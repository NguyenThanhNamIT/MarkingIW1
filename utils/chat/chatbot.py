from antlr4 import *
import sys
import os
import logging
import json
import random

# Add the parent directory to sys.path to find CompiledFiles
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # This goes to utils directory
sys.path.append(parent_dir)

from CompiledFiles.TenseQuizLexer import TenseQuizLexer
from CompiledFiles.TenseQuizParser import TenseQuizParser
from CompiledFiles.TenseQuizListener import TenseQuizListener

class QuizChatbot:
    def __init__(self):
        self.state = "start"
        self.all_questions = [
            # Blank Questions
            {
                "type": "blank",
                "prompt": "Fill in the blank: She ___ (go) to school yesterday.",
                "correct_answers": ["went"],
                "correct_tenses": ["past"]
            },
            {
                "type": "blank",
                "prompt": "Fill in the blank: They ___ (be) happy now.",
                "correct_answers": ["are"],
                "correct_tenses": ["present"]
            },
            {
                "type": "blank",
                "prompt": "Fill in the blank: He ___ (visit) his friend last weekend.",
                "correct_answers": ["visited"],
                "correct_tenses": ["past"]
            },
            {
                "type": "blank",
                "prompt": "Fill in the blank: We ___ (travel) to Japan next month.",
                "correct_answers": ["will travel"],
                "correct_tenses": ["future"]
            },
            # Choose Questions
            {
                "type": "choose",
                "prompt": "Choose the correct tense: She walks daily. 1) past 2) present 3) future 4) none",
                "correct_answers": ["2"],
                "correct_tenses": ["present"]
            },
            {
                "type": "choose",
                "prompt": "Choose the correct tense: He will run tomorrow. 1) past 2) present 3) future 4) none",
                "correct_answers": ["3"],
                "correct_tenses": ["future"]
            },
            {
                "type": "choose",
                "prompt": "Choose the correct tense: They danced at the party. 1) past 2) present 3) future 4) none",
                "correct_answers": ["1"],
                "correct_tenses": ["past"]
            },
            {
                "type": "choose",
                "prompt": "Choose the correct tense: I am reading a book. 1) past 2) present 3) future 4) none",
                "correct_answers": ["2"],
                "correct_tenses": ["present"]
            },
            # Complete Questions
            {
                "type": "complete",
                "prompt": "Complete the sentence: She ___ (study) and ___ (play) every evening.",
                "correct_answers": ["studies", "plays"],
                "correct_tenses": ["present", "present"]
            },
            {
                "type": "complete",
                "prompt": "Complete the sentence: They ___ (go) and ___ (see) the movie next week.",
                "correct_answers": ["will go", "will see"],
                "correct_tenses": ["future", "future"]
            },
            {
                "type": "complete",
                "prompt": "Complete the sentence: He ___ (write) and ___ (draw) in his notebook yesterday.",
                "correct_answers": ["wrote", "drew"],
                "correct_tenses": ["past", "past"]
            },
            {
                "type": "complete",
                "prompt": "Complete the sentence: We ___ (sing) and ___ (dance) at the event tomorrow.",
                "correct_answers": ["will sing", "will dance"],
                "correct_tenses": ["future", "future"]
            },
            # Correct Questions
            {
                "type": "correct",
                "prompt": "Correct the sentence: She go to school yesterday.",
                "correct_answers": ["She went to school yesterday."],
                "correct_verb": "went",
                "correct_tenses": ["past"]
            },
            {
                "type": "correct",
                "prompt": "Correct the sentence: They is playing now.",
                "correct_answers": ["They are playing now."],
                "correct_verb": "are playing",
                "correct_tenses": ["present"]
            },
            {
                "type": "correct",
                "prompt": "Correct the sentence: He write a letter last night.",
                "correct_answers": ["He wrote a letter last night."],
                "correct_verb": "wrote",
                "correct_tenses": ["past"]
            },
            {
                "type": "correct",
                "prompt": "Correct the sentence: We will goes to the park tomorrow.",
                "correct_answers": ["We will go to the park tomorrow."],
                "correct_verb": "will go",
                "correct_tenses": ["future"]
            }
        ]
        self.instructions = {
            "blank": "For Blank questions, fill in the blank with the correct verb form.\nExample: 'He ___ (eat) an apple yesterday.' → Enter: 'ate'",
            "choose": "For Choose questions, select the correct tense by entering the number (1-4).\nExample: 'I sleep well. 1) past 2) present 3) future 4) none' → Enter: '2'",
            "complete": "For Complete questions, enter each verb separately as prompted.\nExample: 'They ___ (run) and ___ (jump) last week.' → First enter: 'ran', then enter: 'jumped'",
            "correct": "For Correct questions, enter the correct verb phrase or the full corrected sentence.\nExample: 'She run fast yesterday.' → Enter: 'ran' or 'She ran fast yesterday.'"
        }        
        self.selected_questions = []
        self.user_responses = []
        self.current_question = 0
        self.selected_option = None
        self.user_answer = None
        self.first_verb_answer = None  # Store the first verb for complete questions
        self.total_score = 0
        self.logger = logging.getLogger(__name__)
          # Setup logging with a relative path
        log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chatbot.log")
        logging.basicConfig(filename=log_file, level=logging.INFO)
          # Load config.json with relative path
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        try:
            with open(config_file, "r") as f:
                self.dialogue = json.load(f)
        except FileNotFoundError:
            # Fallback default dialogue
            self.dialogue = {
                "greetings": ["Hello! I'm your Tense Quiz Chatbot. Type 'start' to begin!"]
            }

    def select_questions(self):
        questions_by_type = {
            "blank": [q for q in self.all_questions if q["type"] == "blank"],
            "choose": [q for q in self.all_questions if q["type"] == "choose"],
            "complete": [q for q in self.all_questions if q["type"] == "complete"],
            "correct": [q for q in self.all_questions if q["type"] == "correct"]
        }
        self.selected_questions = []
        for question_type in questions_by_type:
            selected = random.sample(questions_by_type[question_type], 2)
            self.selected_questions.extend(selected)
        random.shuffle(self.selected_questions)

    def process_input(self, user_input):
        self.logger.info(f"User input: {user_input}")
        if self.state == "start":
            return self.handle_start(user_input)
        elif self.state == "select_option":
            return self.handle_select_option(user_input)
        elif self.state == "answer":
            return self.handle_answer(user_input)
        elif self.state == "answer_first_verb":
            return self.handle_first_verb(user_input)
        elif self.state == "answer_second_verb":
            return self.handle_second_verb(user_input)

    def handle_start(self, user_input):
        user_input = user_input.strip().lower()
        if user_input == "start":
            self.select_questions()
            self.user_responses = []
            self.total_score = 0
            self.state = "select_option"
            question = self.selected_questions[self.current_question]
            return f"{self.instructions[question['type']]}\n\n{question['prompt']}"
        return self.dialogue["greetings"][0]

    def handle_select_option(self, user_input):
        user_input = user_input.strip()
        question = self.selected_questions[self.current_question]
        if question["type"] in ["blank", "correct"]:
            self.state = "answer"
            return "Enter your answer:"
        elif question["type"] == "choose":
            if user_input not in ["1", "2", "3", "4"]:
                return "Please select 1, 2, 3, or 4."
            self.selected_option = int(user_input) - 1
            self.state = "answer"
            return "Enter your answer (e.g., the number of the correct option):"
        elif question["type"] == "complete":
            self.state = "answer_first_verb"
            # Extract the verb from the prompt for the hint
            verb_hint = question["prompt"].split("___")[1].split("and")[0].strip()
            return f"Enter the first verb ({verb_hint}):"

    def handle_first_verb(self, user_input):
        self.first_verb_answer = user_input.strip().lower()
        question = self.selected_questions[self.current_question]
        verb_hint = question["prompt"].split("___")[2].split("at")[0].strip()
        self.state = "answer_second_verb"
        return f"Enter the second verb ({verb_hint}):"

    def handle_second_verb(self, user_input):
        self.user_answer = user_input.strip().lower()
        question = self.selected_questions[self.current_question]
        correct_answer = [ans.lower() for ans in question["correct_answers"]]
        correct_tense = question["correct_tenses"]

        # Combine both answers for evaluation
        user_verbs_combined = [self.first_verb_answer, self.user_answer]
        verb_checks = [user_verbs_combined[i] == correct_answer[i] for i in range(len(correct_answer))]
        is_correct = all(verb_checks)
        correct_verb_count = sum(1 for check in verb_checks if check)
        question_score = correct_verb_count * 0.5

        response = ""
        if not is_correct:
            incorrect_verbs = [f"'{user_verbs_combined[i]}' should be '{correct_answer[i]}'" for i in range(len(verb_checks)) if not verb_checks[i]]
            response = f"One or more verbs are incorrect: {', '.join(incorrect_verbs)}."
        else:
            response = "Đúng"

        self.total_score += question_score
        response_entry = {
            "question": question["prompt"],
            "user_answer": f"{self.first_verb_answer} and {self.user_answer}",
            "is_correct": is_correct,
            "score": question_score,
            "correct_answer": correct_answer,
            "verb_checks": verb_checks
        }
        self.user_responses.append(response_entry)

        self.logger.info(f"User: {self.first_verb_answer} and {self.user_answer}, Correct: {correct_answer}, Response: {response}, Score: {question_score}")

        self.current_question += 1
        if self.current_question < len(self.selected_questions):
            self.state = "select_option"
            question = self.selected_questions[self.current_question]
            response += f"\n\nCâu hỏi tiếp theo:\n{self.instructions[question['type']]}\n\n{question['prompt']}"
        else:
            response += f"\n\nKết thúc trò chơi!\n\n--- Review of Your Answers ---\n"
            for idx, entry in enumerate(self.user_responses, 1):
                correctness = "Correct" if entry["is_correct"] else "Incorrect"
                if entry["question"].startswith("Complete"):
                    verb_statuses = []
                    user_verbs = entry["user_answer"].split(" and ")
                    for i, check in enumerate(entry["verb_checks"]):
                        verb_status = f"Verb {i+1}: {'Correct' if check else 'Incorrect'} (Your answer: '{user_verbs[i]}', Correct: '{entry['correct_answer'][i]}')"
                        verb_statuses.append(verb_status)
                    response += f"Question {idx}: {entry['question']}\nYour Answer: {entry['user_answer']}\nResult: {correctness}\nScore: {entry['score']}/1\nDetails: {'; '.join(verb_statuses)}\n\n"
                else:
                    response += f"Question {idx}: {entry['question']}\nYour Answer: {entry['user_answer']}\nResult: {correctness}\nScore: {entry['score']}/1\n\n"
            response += f"Final Score: {self.total_score}/8"
            self.state = "start"
            self.current_question = 0
        self.logger.info(f"Response: {response}")
        return response

    def handle_answer(self, user_input):
        self.user_answer = user_input.strip().lower()
        question = self.selected_questions[self.current_question]
        correct_answer = [ans.lower() for ans in question["correct_answers"]]
        correct_tense = question["correct_tenses"]

        is_correct = False
        response = ""
        question_score = 0
        verb_checks = None

        if question["type"] == "blank":
            is_correct = self.user_answer in correct_answer
            question_score = 1 if is_correct else 0
        elif question["type"] == "choose":
            is_correct = self.user_answer == correct_answer[0]
            question_score = 1 if is_correct else 0
        elif question["type"] == "correct":
            correct_verb = question.get("correct_verb", "").lower()
            is_correct = (self.user_answer == correct_answer[0]) or (self.user_answer == correct_verb)
            question_score = 1 if is_correct else 0
            if not is_correct:
                response = f"Incorrect. The correct verb phrase is '{correct_verb}' or the full sentence should be '{correct_answer[0]}'."

        if question["type"] in ["blank", "correct"] and self.user_answer in correct_answer:
            input_stream = InputStream(self.user_answer)
            lexer = TenseQuizLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = TenseQuizParser(stream)
            listener = TenseQuizListener()
            walker = ParseTreeWalker()
            walker.walk(listener, parser.answer())
            user_tense = listener.get_tense()

        if response == "":
            response = "Đúng" if is_correct else "Sai"

        self.total_score += question_score
        response_entry = {
            "question": question["prompt"],
            "user_answer": self.user_answer,
            "is_correct": is_correct,
            "score": question_score,
            "correct_answer": correct_answer,
            "verb_checks": verb_checks
        }
        self.user_responses.append(response_entry)

        self.logger.info(f"User: {self.user_answer}, Correct: {correct_answer}, Response: {response}, Score: {question_score}")

        self.current_question += 1
        if self.current_question < len(self.selected_questions):
            self.state = "select_option"
            question = self.selected_questions[self.current_question]
            response += f"\n\nCâu hỏi tiếp theo:\n{self.instructions[question['type']]}\n\n{question['prompt']}"
        else:
            response += f"\n\nKết thúc trò chơi!\n\n--- Review of Your Answers ---\n"
            for idx, entry in enumerate(self.user_responses, 1):
                correctness = "Correct" if entry["is_correct"] else "Incorrect"
                if entry["question"].startswith("Complete"):
                    verb_statuses = []
                    user_verbs = entry["user_answer"].split(" and ")
                    for i, check in enumerate(entry["verb_checks"]):
                        verb_status = f"Verb {i+1}: {'Correct' if check else 'Incorrect'} (Your answer: '{user_verbs[i]}', Correct: '{entry['correct_answer'][i]}')"
                        verb_statuses.append(verb_status)
                    response += f"Question {idx}: {entry['question']}\nYour Answer: {entry['user_answer']}\nResult: {correctness}\nScore: {entry['score']}/1\nDetails: {'; '.join(verb_statuses)}\n\n"
                else:
                    response += f"Question {idx}: {entry['question']}\nYour Answer: {entry['user_answer']}\nResult: {correctness}\nScore: {entry['score']}/1\n\n"
            response += f"Final Score: {self.total_score}/8"
            self.state = "start"
            self.current_question = 0
        self.logger.info(f"Response: {response}")
        return response
