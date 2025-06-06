from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
import sys
import os
import uuid

# Add the parent directory to the Python path to access utils
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.chat.chatbot import QuizChatbot

app = Flask(__name__)

# Configure Flask session
app.config['SECRET_KEY'] = '123'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = 'flask_session'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True

# Initialize session
Session(app)

# Enable CORS for all domains and routes
CORS(app, supports_credentials=True)

# Store chatbot instances per session
chatbot_sessions = {}

def get_or_create_chatbot():
    """Get or create a chatbot instance for the current session"""
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    
    session_id = session['session_id']
    
    if session_id not in chatbot_sessions:
        chatbot_sessions[session_id] = QuizChatbot()
    
    return chatbot_sessions[session_id]

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Tense Quiz API is running"})

@app.route('/api/start', methods=['POST'])
def start_game():
    """Start a new quiz game"""
    chatbot = get_or_create_chatbot()
    response = chatbot.process_input("start")
    
    current_question_data = None
    if (chatbot.selected_questions and 
        chatbot.current_question < len(chatbot.selected_questions)):
        question = chatbot.selected_questions[chatbot.current_question]
        current_question_data = {
            "type": question["type"],
            "prompt": question["prompt"],
            "instruction": chatbot.instructions.get(question["type"], "")
        }
    
    return jsonify({
        "success": True,
        "message": response,
        "state": chatbot.state,
        "current_question": chatbot.current_question,
        "total_questions": len(chatbot.selected_questions) if chatbot.selected_questions else 0,
        "current_question_data": current_question_data
    })

@app.route('/api/answer', methods=['POST'])
def submit_answer():
    """Submit an answer to the current question"""
    data = request.get_json()
    
    if not data or 'answer' not in data:
        return jsonify({"success": False, "error": "Answer is required"}), 400
    
    user_answer = data['answer']
    chatbot = get_or_create_chatbot()
    
    try:
        # If we're in select_option state, transition to the appropriate answer state first
        if chatbot.state == "select_option":
            question = chatbot.selected_questions[chatbot.current_question]
            if question["type"] in ["blank", "correct"]:
                chatbot.state = "answer"
            elif question["type"] == "choose":
                chatbot.state = "answer" 
            elif question["type"] == "complete":
                chatbot.state = "answer_first_verb"
        
        response = chatbot.process_input(user_answer)
        
        # Get next question data if available
        current_question_data = None
        if (chatbot.selected_questions and 
            chatbot.current_question < len(chatbot.selected_questions)):
            question = chatbot.selected_questions[chatbot.current_question]
            current_question_data = {
                "type": question["type"],
                "prompt": question["prompt"],
                "instruction": chatbot.instructions.get(question["type"], "")
            }
        
        return jsonify({
            "success": True,
            "message": response,
            "state": chatbot.state,
            "current_question": chatbot.current_question,
            "total_questions": len(chatbot.selected_questions) if chatbot.selected_questions else 0,
            "total_score": chatbot.total_score,
            "current_question_data": current_question_data
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get current game status"""
    chatbot = get_or_create_chatbot()
    
    current_question_data = None
    if (chatbot.selected_questions and 
        chatbot.current_question < len(chatbot.selected_questions)):
        question = chatbot.selected_questions[chatbot.current_question]
        current_question_data = {
            "type": question["type"],
            "prompt": question["prompt"],
            "instruction": chatbot.instructions.get(question["type"], "")
        }
    
    return jsonify({
        "state": chatbot.state,
        "current_question": chatbot.current_question,
        "total_questions": len(chatbot.selected_questions) if chatbot.selected_questions else 0,
        "total_score": chatbot.total_score,
        "current_question_data": current_question_data
    })

@app.route('/api/reset', methods=['POST'])
def reset_game():
    """Reset the current game"""
    # Clear the session-based chatbot instance
    if 'session_id' in session:
        session_id = session['session_id']
        if session_id in chatbot_sessions:
            del chatbot_sessions[session_id]
    
    # Clear the session completely to start fresh
    session.clear()
    
    # Create a new chatbot instance
    chatbot = get_or_create_chatbot()
    
    return jsonify({
        "success": True,
        "message": "Game reset successfully",
        "state": chatbot.state
    })

@app.route('/api/results', methods=['GET'])
def get_results():
    """Get the results of the completed game"""
    chatbot = get_or_create_chatbot()
    
    if not chatbot.user_responses:
        return jsonify({"success": False, "error": "No completed game found"}), 404
    
    detailed_results = []
    for idx, entry in enumerate(chatbot.user_responses, 1):
        result = {
            "question_number": idx,
            "question": entry["question"],
            "user_answer": entry["user_answer"],
            "is_correct": entry["is_correct"],
            "score": entry["score"],
            "correct_answer": entry["correct_answer"]
        }
        
        # Add verb checks for complete questions
        if entry.get("verb_checks"):
            result["verb_checks"] = entry["verb_checks"]
        
        detailed_results.append(result)
    
    return jsonify({
        "success": True,
        "total_score": chatbot.total_score,
        "max_score": 8,
        "percentage": round((chatbot.total_score / 8) * 100, 2),
        "detailed_results": detailed_results
    })

@app.route('/api/instructions', methods=['GET'])
def get_instructions():
    """Get instructions for all question types"""
    chatbot = get_or_create_chatbot()
    
    return jsonify({
        "success": True,
        "instructions": chatbot.instructions
    })

@app.route('/api/questions', methods=['GET'])
def get_all_questions():
    """Get all available questions (for admin/debug purposes)"""
    chatbot = get_or_create_chatbot()
    
    return jsonify({
        "success": True,
        "all_questions": chatbot.all_questions,
        "selected_questions": chatbot.selected_questions if chatbot.selected_questions else []
    })

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
