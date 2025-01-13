# Sentiment Analysis Web Application - React & FastAPI

This project is a full-stack application that performs sentiment analysis on textual data. The backend is developed using **FastAPI**, and the front end is built using **React**. The application accepts text input (in the form of CSV files) and provides sentiment analysis (positive, neutral, or negative) for each entry.The results are displayed in a visual format (e.g., bar charts, pie charts) for easy understanding.

# Backend - FastAPI

<font size="10">**Overview**</font>
The backend API is built using FastAPI, a high-performance web framework for building APIs with Python 3.10+ based on standard Python-type hints. We use **TextBlob** for sentiment analysis and **JWT authentication** to secure the endpoints. The API exposes endpoints to analyze individual text inputs as well as CSV files containing multiple entries.

**Installation**

1) Clone the repository:
```bash
#!bash

git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app/backend

2) Install required dependencies:
```bash
#!bash
pip install -r requirements.txt

3) Start the FastAPI server:
```bash
#!bash
uvicorn API:app --reload

The FastAPI backend will be available at http://localhost:8000.

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
















