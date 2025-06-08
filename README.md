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
└── utils/                    # Core game logic and utilities
    ├── run.py               # ANTLR generator and grammar tester
    ├── grammar_validator.py # Grammar validation module
    ├── TenseQuiz.g4         # ANTLR grammar file
    └── CompiledFiles/       # ANTLR generated files
```

## Features

- **Multiple Question Types:**
  - **Blank**: Fill in the blank with correct verb forms
  - **Correct**: Fix grammatically incorrect sentences and rewrite the sentence

- **Modern Web Interface:**
  - Next.js with TypeScript
  - Responsive design with Tailwind CSS
  - Real-time feedback
  - Progress tracking
  - Detailed results review

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
cd utils
# Generate ANTLR parser files from grammar
python run.py gen

# Run comprehensive grammar tests
python run.py test

# Validate a specific sentence
python run.py validate "Your sentence here"
```

**Note:** Before running the generator, ensure you have ANTLR 4 installed and update the `ANTLR_JAR` path in `utils/run.py` to match your ANTLR installation location.

### 2. Start the Server

```powershell
# Navigate to server directory
cd server

# Create and activate virtual environment (optional but recommended)
python -m venv .venv
.\.venv\Scripts\Activate

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

### 2. Correct Questions
Enter either the correct verb phrase or the full corrected sentence.
- **Example**: "She go to school yesterday."
- **Answer**: "She went to school yesterday."

### Architecture

The application uses a clean separation between frontend and backend:

- **Frontend (Next.js)**: Modern React-based interface with TypeScript
- **Backend (Flask)**: RESTful API with session management
- **Core Logic (utils)**: ANTLR-based grammar parsing, validation utilities, and tense analysis

### Adding New Questions

To add new questions, edit the question data files in the server directory or modify the quiz logic:

```python
{
    "type": "blank",  # or "correct"
    "prompt": "Your question text with ___ (verb) placeholder",
}
```

### Adding New Grammar Rules

To extend the grammar parser:

1. **Edit Grammar File:**
   ```powershell
   # Edit utils/TenseQuiz.g4
   # Add new grammar rules, vocabulary, or patterns
   ```

2. **Regenerate Parser:**
   ```powershell
   cd utils
   python run.py gen
   ```

3. **Test Changes:**
   ```powershell
   python run.py test
   python run.py validate "your test sentence"
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

## License

This project is developed for educational purposes as part of the Principle of Programming Language (PPL) course.

---

*Last updated: June 2025*
