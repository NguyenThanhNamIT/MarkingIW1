import json
import logging
from antlr4 import *
from TenseQuizLexer import TenseQuizLexer
from TenseQuizParser import TenseQuizParser
from TenseQuizListener import TenseQuizListener

class QuizChatbot:
    def __init__(self):
        self.state = "start"
        self.questions = [
            {
                "prompt": "Choose the correct tense:\n1. She ___ (go) to school yesterday.\n2. She ___ (go) to school every day.",
                "correct_answers": ["went", "goes"],
                "correct_tenses": ["past", "present"]
            },
            {
                "prompt": "Choose the correct tense:\n1. They ___ (be) happy tomorrow.\n2. They ___ (be) happy now.",
                "correct_answers": ["will be", "are"],
                "correct_tenses": ["future", "present"]
            }
        ]
        self.current_question = 0
        self.selected_option = None
        self.user_answer = None
        self.score = 0
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename="chatbot.log", level=logging.INFO)
        with open("config.json", "r") as f:
            self.dialogue = json.load(f)

    def process_input(self, user_input):
        self.logger.info(f"User input: {user_input}")
        if self.state == "start":
            return self.handle_start(user_input)
        elif self.state == "select_option":
            return self.handle_select_option(user_input)
        elif self.state == "answer":
            return self.handle_answer(user_input)

    def handle_start(self, user_input):
        user_input = user_input.strip().lower()
        if user_input == "start game":
            self.state = "select_option"
            return self.questions[self.current_question]["prompt"]
        return self.dialogue["greetings"][0]

    def handle_select_option(self, user_input):
        user_input = user_input.strip()
        if user_input not in ["1", "2"]:
            return "Please select 1 or 2."
        self.selected_option = int(user_input) - 1
        self.state = "answer"
        return "Enter your answer (e.g., 'went') for the blank:"

    def handle_answer(self, user_input):
        self.user_answer = user_input.strip().lower()
        correct_answer = self.questions[self.current_question]["correct_answers"][self.selected_option]
        correct_tense = self.questions[self.current_question]["correct_tenses"][self.selected_option]

        # Parse user answer to determine tense
        input_stream = InputStream(self.user_answer)
        lexer = TenseQuizLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = TenseQuizParser(stream)
        listener = TenseQuizListener()
        walker = ParseTreeWalker()
        walker.walk(listener, parser.answer())
        user_tense = listener.get_tense()

        # Debug: Log the user input and detected tense
        self.logger.info(f"User input: {self.user_answer}, Detected tense: {user_tense}, Expected tense: {correct_tense}")

        # Check if answer and tense are correct
        if user_tense is None:
            is_correct = False  # If tense cannot be determined, mark as incorrect
        else:
            is_correct = (self.user_answer == correct_answer) and (user_tense == correct_tense)
        response = "Đúng" if is_correct else "Sai"
        self.logger.info(f"User: {self.user_answer}, Correct: {correct_answer}, User tense: {user_tense}, Correct tense: {correct_tense}, Response: {response}")

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.state = "select_option"
            response += f"\n\nCâu hỏi tiếp theo:\n{self.questions[self.current_question]['prompt']}"
        else:
            response += f"\n\nKết thúc trò chơi!"
            self.state = "start"
            self.current_question = 0
            self.score = 0
        self.logger.info(f"Response: {response}")
        return response