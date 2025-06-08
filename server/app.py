from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
import sys
import os
import uuid
import json
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.grammar_validator import validate_sentence

app = Flask(__name__)

# Configure Flask session
app.config['SECRET_KEY'] = '123'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = 'flask_session'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True

# Initialize session
Session(app)
CORS(app, supports_credentials=True)

# Load questions from JSON file
def load_questions():
    """Load questions from the JSON file"""
    try:
        with open(os.path.join(os.path.dirname(__file__), 'data', 'questions.json'), 'r') as file:
            data = json.load(file)
            return data['questions'], data['instructions']
    except Exception as e:
        print(f"Error loading questions: {e}")
        return [], {}

QUESTIONS, INSTRUCTIONS = load_questions()

def get_random_question():
    if not QUESTIONS:
        return None
    
    used_questions = session.get('used_questions', [])
    if len(used_questions) >= len(QUESTIONS) or len(used_questions) >= 10:
        return None
    
    available_questions = [q for q in QUESTIONS if q['id'] not in used_questions]
    
    if not available_questions:
        return None
    
    return random.choice(available_questions)

def initialize_game_session():
    session['game_id'] = str(uuid.uuid4())
    session['current_question'] = None
    session['score'] = 0
    session['total_questions'] = 0
    session['answers_history'] = []
    session['game_active'] = True
    session['used_questions'] = []  # Track used question IDs
    session['max_questions'] = 10
    return session['game_id']

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Tense Quiz API is running"})

@app.route('/api/start', methods=['POST'])
def start_game():
    """Start a new quiz game"""
    try:
        game_id = initialize_game_session()
        question = get_random_question()
        if not question:
            return jsonify({
                "success": False,
                "error": "No questions available"
            }), 500
        
        session['current_question'] = question
        session['used_questions'].append(question['id'])
        
        return jsonify({
            "success": True,
            "message": "Game started successfully",
            "game_id": game_id,
            "question": {
                "id": question['id'],
                "type": question['type'],
                "prompt": question['prompt']
            },
            "score": 0,
            "total_questions": 0,
            "max_questions": session['max_questions']
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Failed to start game: {str(e)}"
        }), 500

@app.route('/api/answer', methods=['POST'])
def submit_answer():
    """Submit an answer to the current question"""
    try:
        if not session.get('game_active'):
            return jsonify({
                "success": False,
                "error": "No active game. Please start a new game."
            }), 400
        
        # Get the answer from request
        data = request.get_json()
        if not data or 'answer' not in data:
            return jsonify({
                "success": False,
                "error": "Answer is required"
            }), 400
        
        user_answer = data['answer'].strip()
        current_question = session.get('current_question')
        if not current_question:
            return jsonify({
                "success": False,
                "error": "No current question found"
            }), 400
        
        # Validate the answer using ANTLR grammar parser
        current_question = session.get('current_question')
        question_type = current_question.get('type', '')
        question_prompt = current_question.get('prompt', '').lower()
        
        # Use grammar validator to check the answer
        validation_result = validate_sentence(user_answer)
        is_correct = validation_result['is_valid']
        
        if question_type == 'correct':
            words = user_answer.strip().split()
            if len(words) < 3:  # Too short for a complete sentence
                is_correct = False
                validation_result['message'] = 'Answer too short for a complete sentence'        
        elif question_type == 'blank':
            words = user_answer.strip().split()
            if len(words) > 3:  # Too long for fill-in-the-blank
                is_correct = False
                validation_result['message'] = 'Answer too long for fill-in-the-blank question'
        
        feedback = ""
        
        if is_correct:
            session['score'] += 1
            feedback = f"✅ Correct! {validation_result.get('message', '')}"
        else:
            feedback = f"❌ Incorrect answer: '{user_answer}'"
        session['total_questions'] += 1
        session['answers_history'].append({
            'question': current_question,
            'user_answer': user_answer,
            'is_correct': is_correct,
            'feedback': feedback
        })
        max_questions = session.get('max_questions', 10)
        game_complete = session['total_questions'] >= max_questions
        
        next_question = None
        if not game_complete:
            next_question = get_random_question()
            if next_question:
                session['current_question'] = next_question
                session['used_questions'].append(next_question['id'])  # Track used question
            else:
                game_complete = True  # No more questions available
        
        if game_complete:
            session['game_active'] = False
        
        response_data = {
            "success": True,
            "is_correct": is_correct,
            "feedback": feedback,
            "score": session['score'],
            "total_questions": session['total_questions'],
            "max_questions": session.get('max_questions', 10)
        }
        
        if next_question and not game_complete:
            response_data["next_question"] = {
                "id": next_question['id'],
                "type": next_question['type'],
                "prompt": next_question['prompt']
            }
        else:
            response_data["game_complete"] = True
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Failed to process answer: {str(e)}"
        }), 500


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get current game status"""
    try:
        if not session.get('game_active'):
            return jsonify({
                "success": True,
                "game_active": False,
                "message": "No active game"
            })
        
        current_question = session.get('current_question')
        return jsonify({
            "success": True,
            "game_active": True,
            "game_id": session.get('game_id'),
            "score": session.get('score', 0),
            "total_questions": session.get('total_questions', 0),
            "max_questions": session.get('max_questions', 10),
            "current_question": {
                "id": current_question['id'],
                "type": current_question['type'],
                "prompt": current_question['prompt']
            } if current_question else None
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Failed to get status: {str(e)}"
        }), 500

@app.route('/api/reset', methods=['POST'])
def reset_game():
    """Reset the current game"""
    try:
        session.clear()
        
        return jsonify({
            "success": True,
            "message": "Game reset successfully"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Failed to reset game: {str(e)}"
        }), 500

@app.route('/api/results', methods=['GET'])
def get_results():
    try:
        if not session.get('answers_history'):
            return jsonify({
                "success": False,
                "error": "No game results available"
            }), 400
        
        answers_history = session.get('answers_history', [])
        score = session.get('score', 0)
        total_questions = session.get('total_questions', 0)
        accuracy = (score / total_questions * 100) if total_questions > 0 else 0
        
        return jsonify({
            "success": True,
            "results": {
                "score": score,
                "total_questions": total_questions,
                "accuracy": round(accuracy, 2),
                "answers_history": answers_history
            }
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Failed to get results: {str(e)}"
        }), 500

@app.route('/api/instructions', methods=['GET'])
def get_instructions():
    try:
        return jsonify({
            "success": True,
            "instructions": INSTRUCTIONS,
            "total_questions_available": len(QUESTIONS)
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Failed to get instructions: {str(e)}"
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"success": False, "error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"success": False, "error": "Internal server error"}), 500

if __name__ == '__main__':
    print("Tense Quiz API Server Startup")
    print("=" * 40)
    # Create necessary directories
    os.makedirs('flask_session', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=8000)
