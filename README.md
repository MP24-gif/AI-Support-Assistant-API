
# AI Support Assistant API

## Project Overview

AI Support Assistant API is a REST API built with FastAPI and Groq LLM integration. It accepts IT support questions and returns AI-generated troubleshooting guidance.

The project demonstrates API development, input validation, external AI integration, error handling, and automated testing.

## Features

- REST API built with FastAPI
- AI-powered IT support responses using Groq
- Request validation using Pydantic
- Centralized handling of model provider errors
- Environment-based API key configuration
- Automated API tests using pytest
- Interactive API documentation using Swagger UI

## Technology Stack

- Python
- FastAPI
- Pydantic
- Groq API
- pytest
- HTTPX
- python-dotenv

## Project Structure

```text
AI Support Assistant API/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── llm.py
├── tests/
│   └── test_api.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/MP24-gif/AI-Support-Assistant-API.git
cd AI-Support-Assistant-API
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a local `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own Groq API key. Never commit your real API key to GitHub.

## Run the Application

Start the development server:

```bash
python -m uvicorn app.main:app --reload
```

Open the following URL in your browser:

http://127.0.0.1:8000/docs

Swagger UI lets you explore and test the API endpoints.

## API Endpoints

### Health Check

`GET /health`

Checks whether the API is running.

### Submit an IT Support Question

`POST /support`

Example request:

```json
{
  "question": "My laptop cannot connect to Wi-Fi"
}
```

The API returns a structured response containing the request status, question, and AI-generated answer, according to the application's response model.

## Error Handling

The application handles invalid requests and model-provider failures with appropriate HTTP status codes, including:

- `422` — Request validation failure
- `502` — Model provider error
- `503` — Provider connection failure
- `504` — Provider timeout

## Run Automated Tests

Execute the test suite:

```bash
python -m pytest -v
```

Tests cover health checks, successful support requests, request validation, and error handling.

## Security Notes

- Keep API credentials in environment variables.
- Do not commit `.env` or virtual environment files.
- Do not expose API keys in source code, logs, or documentation.

## Learning Outcomes

This project demonstrates practical experience with REST API development, LLM integration, request validation, exception handling, and automated testing.
