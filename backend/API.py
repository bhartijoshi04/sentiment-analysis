from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from textblob import TextBlob
import time
import pandas as pd
import io
from fastapi.middleware.cors import CORSMiddleware


# Constants for authentication
SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock user database
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "hashed_password": pwd_context.hash("testpassword"),
    }
}

# FastAPI app instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, replace with ['http://localhost:3000'] for more restricted access
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Utility functions for authentication
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and verify_password(password, user["hashed_password"]):
        return user
    return None

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    expire = time.time() + (expires_delta or ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependency to get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Authentication endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Sentiment analysis input model
class SentimentRequest(BaseModel):
    text: str

# Sentiment analysis output model
class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    polarity: float
    subjectivity: float

# Sentiment analysis endpoint
@app.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(
    request: SentimentRequest, current_user: str = Depends(get_current_user)
):
    blob = TextBlob(request.text)
    sentiment = "positive" if blob.polarity > 0 else "negative" if blob.polarity < 0 else "neutral"
    return SentimentResponse(
        text=request.text,
        sentiment=sentiment,
        polarity=blob.polarity,
        subjectivity=blob.subjectivity,
    )

# CSV analysis input model
class CSVAnalysisResult(BaseModel):
    id: int
    text: str
    timestamp: str
    sentiment: str
    polarity: float
    subjectivity: float

# CSV upload and analysis endpoint
@app.post("/analyze-csv/")
async def analyze_csv(file: UploadFile = File(...), current_user: str = Depends(get_current_user)):
    try:
        # Read the uploaded CSV file
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # Validate if necessary columns are present
        if not all(col in df.columns for col in ['id', 'text', 'timestamp']):
            raise HTTPException(status_code=400, detail="CSV must contain 'id', 'text', and 'timestamp' columns.")

        results = []

        # Process each row and analyze sentiment
        for index, row in df.iterrows():
            blob = TextBlob(row['text'])
            sentiment = "positive" if blob.polarity > 0 else "negative" if blob.polarity < 0 else "neutral"
            results.append(CSVAnalysisResult(
                id=row['id'],
                text=row['text'],
                timestamp=row['timestamp'],
                sentiment=sentiment,
                polarity=blob.polarity,
                subjectivity=blob.subjectivity
            ))

        return {"results": [result.dict() for result in results]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing CSV file: {e}")

# Test endpoint to check user authentication
@app.get("/users/me")
async def read_users_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}
