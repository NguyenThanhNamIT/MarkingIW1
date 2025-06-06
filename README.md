# English Tense Quiz Game

A complete English tense quiz application with a Python Flask backend API and a modern web frontend.

## Project Structure

```
QuizGameChatbot/
├── README.md                 # This file
├── client/                   # Next.js frontend application
│   ├── package.json         # Node.js dependencies
│   ├── next.config.ts       # Next.js configuration
│   ├── tsconfig.json        # TypeScript configuration
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx     # Home page
│   │   │   ├── quiz/
│   │   │   │   └── page.tsx # Quiz interface
│   │   │   └── results/
│   │   │       └── page.tsx # Results page
│   │   └── api/
│   │       └── config.ts    # API configuration
│   └── public/              # Static assets
├── server/                   # Flask backend API server
│   ├── app.py               # Flask API application
│   ├── requirements.txt     # Python dependencies
│   ├── README.md            # Server documentation
│   └── flask_session/       # Session storage
└── utils/                    # Core game logic and utilities
    ├── main.py              # Main entry point
    ├── run.py               # Grammar generator
    ├── TenseQuiz.g4         # ANTLR grammar file
    ├── chat/
    │   ├── chatbot.py       # Main game logic
    │   ├── config.json      # Configuration
    │   └── chatbot.log      # Game logs
    └── CompiledFiles/       # ANTLR generated files
        ├── TenseQuizLexer.py
        ├── TenseQuizParser.py
        └── TenseQuizListener.py
```

## Features

- **Multiple Question Types:**
  - **Blank**: Fill in the blank with correct verb forms
  - **Choose**: Select the correct tense from multiple choices
  - **Complete**: Enter two verbs for compound sentences
  - **Correct**: Fix grammatically incorrect sentences

- **Modern Web Interface:**
  - Next.js with TypeScript
  - Responsive design with Tailwind CSS
  - Real-time feedback
  - Progress tracking
  - Detailed results review

- **Advanced Features:**
  - ANTLR-based grammar parsing for tense analysis
  - Session-based state management
  - Comprehensive error handling
  - Detailed logging and debugging

- **RESTful API:**
  - Flask backend with session management
  - Comprehensive endpoints
  - Error handling
  - CORS support

## Quick Start

### Prerequisites

- Python 3.7 or higher
- Node.js and npm
- A modern web browser

### 1. Generate the ANTLR Grammar
```powershell
# Navigate to utils directory
cd utils

# Run the generator
python run.py gen
```

### 2. Start the Server

```powershell
# Navigate to server directory
cd server

# Create and activate virtual environment (optional but recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

The API server will start on `http://localhost:8000`

### 3. Start the Client

Open a new PowerShell window:

```powershell
# Navigate to client directory
cd client

# Install Node.js dependencies
npm install

# Start the development server
npm run dev
```

The web interface will be available at `http://localhost:3000`

### 4. Play the Game

1. Open your browser and go to `http://localhost:3000`
2. Click "Start Quiz" to begin
3. Follow the instructions for each question type
4. Submit your answers and see immediate feedback
5. Review your complete results at the end

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

### Configuration

- Modify `utils/chat/config.json` to change greeting messages
- Edit question sets in `utils/chat/chatbot.py` to add new questions
- Adjust scoring logic in the chatbot class methods
- Customize the ANTLR grammar in `utils/TenseQuiz.g4` for tense parsing

### Architecture

The application uses a clean separation between frontend and backend:

- **Frontend (Next.js)**: Modern React-based interface with TypeScript
- **Backend (Flask)**: RESTful API with session management
- **Core Logic (utils)**: Game logic, ANTLR parsing, and chatbot implementation

### Adding New Questions

To add new questions, edit the `all_questions` array in `utils/chat/chatbot.py`:

```python
{
    "type": "blank",  # or "choose", "complete", "correct"
    "prompt": "Your question text with ___ (verb) placeholder",
    "correct_answers": ["expected", "answers"],
    "correct_tenses": ["past", "present", "future"]
}
```

## Technology Stack

### Frontend
- **Next.js 14** - React framework with server-side rendering
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **React Hooks** - State management and effects

### Backend
- **Flask** - Python web framework
- **Flask-Session** - Session management
- **Flask-CORS** - Cross-origin resource sharing

### Core Technologies
- **ANTLR 4** - Grammar-based parsing for tense analysis
- **Python 3.7+** - Backend runtime
- **Node.js** - Frontend runtime

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is developed for educational purposes as part of the Principle of Programming Language (PPL) course.

---

*Last updated: June 2025*
