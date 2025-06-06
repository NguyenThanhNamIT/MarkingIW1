# English Tense Quiz Game

A complete English tense quiz application with a Python Flask backend API and a modern web frontend.

## Project Structure

```
QuizGameChatbot/
├── README.md                 # This file
├── client/                   # Frontend web application
│   ├── index.html           # Main web interface
│   └── start_client.py      # Simple HTTP server for client
├── server/                   # Backend API server
│   ├── app.py              # Flask API application
│   ├── requirements.txt    # Python dependencies
│   ├── start_server.py     # Server startup script
│   ├── test_client.py      # API testing script
│   └── README.md           # Server documentation
└── utils/                   # Core game logic and utilities
    ├── Chat/
    │   ├── chatbot.py      # Main game logic
    │   ├── config.json     # Configuration
    │   └── chatbot.log     # Game logs
    ├── CompiledFiles/      # ANTLR generated files
    └── TenseQuiz.g4        # ANTLR grammar file
```

## Features

- **Multiple Question Types:**
  - **Blank**: Fill in the blank with correct verb forms
  - **Choose**: Select the correct tense from multiple choices
  - **Complete**: Enter two verbs for compound sentences
  - **Correct**: Fix grammatically incorrect sentences

- **Modern Web Interface:**
  - Responsive design
  - Real-time feedback
  - Progress tracking
  - Detailed results review

- **RESTful API:**
  - Session management
  - Comprehensive endpoints
  - Error handling
  - CORS support

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- A modern web browser

### 1. Start the API Server

```powershell
# Navigate to server directory
cd server

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

The API server will start on `http://localhost:8000`

### 2. Start the Web Client

Open a new PowerShell window:

```powershell
# Navigate to client directory
cd client

# Start the client server

```

The web interface will be available at `http://localhost:3000`

### 3. Play the Game

1. Open your browser and go to `http://localhost:3000`
2. Click "Start Quiz" to begin
3. Follow the instructions for each question type
4. Submit your answers and see immediate feedback
5. Review your complete results at the end

## Legacy Setup (Original CLI Version)

1. Install Python 3.13.2, ensure PATH includes Scripts.
2. Run: `python utils\run.py gen` to generate the ANTLR grammar.
3. Run: `python utils\main.py` to start the original CLI game.

### Legacy Usage
- Nhập "start" để bắt đầu trò chơi.
- Chọn 1 hoặc 2 để chọn câu hỏi phù hợp
- Nếu đúng thì sẽ qua câu tiếp theo

## API Endpoints

The Flask API provides the following endpoints:

- `GET /api/health` - Server health check
- `POST /api/start` - Start a new quiz game
- `POST /api/answer` - Submit an answer
- `GET /api/status` - Get current game status
- `POST /api/reset` - Reset the current game
- `GET /api/results` - Get detailed results
- `GET /api/instructions` - Get question instructions

## Question Types Explained

### 1. Blank Questions
Fill in the blank with the correct verb form.
- **Example**: "She ___ (go) to school yesterday."
- **Answer**: "went"

### 2. Choose Questions
Select the correct tense by entering 1, 2, 3, or 4.
- **Example**: "She walks daily. 1) past 2) present 3) future 4) none"
- **Answer**: "2"

### 3. Complete Questions
Enter each verb separately when prompted.
- **Example**: "They ___ (run) and ___ (jump) last week."
- **First Answer**: "ran"
- **Second Answer**: "jumped"

### 4. Correct Questions
Enter either the correct verb phrase or the full corrected sentence.
- **Example**: "She go to school yesterday."
- **Answer**: "went" or "She went to school yesterday."

## Development

### Testing the API

Use the provided test client to verify API functionality:

```powershell
cd server
python test_client.py
```

### Configuration

- Modify `utils/Chat/config.json` to change greeting messages
- Edit question sets in `chatbot.py` to add new questions
- Adjust scoring logic in the chatbot class methods

## Troubleshooting

### Common Issues

1. **Server won't start**: Check if Python and pip are installed correctly
2. **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Client can't connect**: Verify the API server is running on port 5000
4. **CORS errors**: The server includes CORS headers, but check browser console for details

### Logs

- Game activity is logged to `utils/Chat/chatbot.log`
- Server logs appear in the console where you started `app.py`


