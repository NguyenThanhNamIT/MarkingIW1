# Tense Quiz API Server

A Flask-based REST API for the Tense Quiz Chatbot application.

## Setup

1. Install dependencies:
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the server:
```bash
python app.py
```

The server will start on `http://localhost:8000`

## API Endpoints

### Base URL: `http://localhost:8000/api`

### 1. Health Check
- **GET** `/health`
- Returns server status

### 2. Start Game
- **POST** `/start`
- Starts a new quiz game
- Returns: Game status and first question

### 3. Submit Answer
- **POST** `/answer`
- Body: `{"answer": "user_answer"}`
- Submits an answer to the current question
- Returns: Result and next question (if any)

### 4. Get Status
- **GET** `/status`
- Returns current game state and progress

### 5. Reset Game
- **POST** `/reset`
- Resets the current game session

### 6. Get Results
- **GET** `/results`
- Returns detailed results of completed game

### 7. Get Instructions
- **GET** `/instructions`
- Returns instructions for all question types

### 8. Get Questions (Admin)
- **GET** `/questions`
- Returns all available questions

## Game Flow

1. Call `/start` to begin a new game
2. Use `/answer` to submit answers
3. Check `/status` for current progress
4. Get `/results` when game is complete
5. Use `/reset` to start over

## Session Management

The API uses Flask sessions to maintain separate game states for different clients. Each session gets its own chatbot instance.

## Question Types

- **blank**: Fill in the blank with correct verb form
- **choose**: Select correct tense (1-4)
- **complete**: Enter two verbs separately
- **correct**: Provide correct verb phrase or full sentence

## Example Usage

```javascript
// Start game
fetch('/api/start', {method: 'POST'})
  .then(response => response.json())
  .then(data => console.log(data.message));

// Submit answer
fetch('/api/answer', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({answer: 'went'})
})
  .then(response => response.json())
  .then(data => console.log(data.message));
```
