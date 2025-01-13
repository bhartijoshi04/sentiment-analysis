# Sentiment Analysis Web Application - React & FastAPI

This project is a full-stack application that performs sentiment analysis on textual data. The backend is developed using **FastAPI**, and the front end is built using **React**. The application accepts text input (in the form of CSV files) and provides sentiment analysis (positive, neutral, or negative) for each entry. The results are displayed in a visual format (e.g., bar charts, pie charts) for easy understanding.

# Backend - FastAPI

<font size="10">**Overview**</font>
The backend API is built using FastAPI, a high-performance web framework for building APIs with Python 3.10+ based on standard Python-type hints. We use **TextBlob** for sentiment analysis and **JWT authentication** to secure the endpoints. The API exposes endpoints to analyze individual text inputs as well as CSV files containing multiple entries.

**Installation**

1) Clone the repository:
```bash
#!bash

git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app/backend
```

2) Install required dependencies:

```bash
#bash
pip install -r requirements.txt
```

3) Start the FastAPI server:
```bash
#!bash
uvicorn API:app --reload
```

The FastAPI backend will be available at **http://localhost:8000**.

# API Endpoints
1) **POST /token - User Authentication**
This endpoint generates a JWT token after authenticating the user. The token will be used for all subsequent requests to the protected API endpoints.
2) **POST /analyze - Sentiment Analysis for Text**
This endpoint analyzes the sentiment of a single piece of text and returns the sentiment score and polarity.
3) **POST /analyze-csv - Sentiment Analysis for CSV File**
This endpoint accepts a CSV file with id, text, and timestamp columns. The file is processed, and sentiment analysis results are returned for each row.
The CSV file is parsed, and sentiment analysis is performed on each text entry using **TextBlob**.
The result for each entry includes the sentiment (positive, neutral, negative), polarity score, and subjectivity score.

# Frontend - React
**Installation**
1) Install frontend dependencies:

```bash
#!bash

npm install
```
2) Start the React development server:

```bash
#!bash
npm start
```
The React frontend will be available at **http://localhost:3000.**

# Components Overview
1) **FileUpload Component**
This component allows users to upload a CSV file containing text data. The file is sent to the backend API (/analyze-csv) for sentiment analysis.

**How It Works:**
-Users choose a file from their computer.
-The file is sent to the backend via an API request using axios.
-The results of the sentiment analysis are displayed once the response is received.

2) **ResultVisualization Component**
This component generates a visual representation of the sentiment distribution using Chart.js.

**How It Works:**
It takes the sentiment analysis data (positive, neutral, negative) and visualizes it using a pie or bar chart.
The chart updates dynamically based on the data returned from the backend.

# Conclusion
Conclusion
This application allows users to perform sentiment analysis on text and visualize the results in an interactive dashboard. The backend, built with FastAPI, handles user authentication, text analysis, and CSV file processing. The front end, built with React, provides a user-friendly interface for uploading files and viewing the results.


















