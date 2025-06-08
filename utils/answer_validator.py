"""
Answer Validator for Quiz Game Chatbot
Validates user answers for grammar correctness
"""

from grammar_validator import validate_sentence, is_grammar_correct, format_grammar_feedback


class AnswerValidator:
    """
    Class to validate quiz answers for grammar correctness
    """
    
    def __init__(self):
        self.validation_history = []
    
    def validate_answer(self, user_answer, expected_type="sentence"):
        """
        Validates a user's answer for grammar correctness
        
        Args:
            user_answer (str): The user's answer to validate
            expected_type (str): Type of answer expected ('sentence' or 'fill_blank')
            
        Returns:
            dict: Validation result with feedback
        """
        if not user_answer or not user_answer.strip():
            return {
                'is_valid': False,
                'score': 0,
                'feedback': "Please provide an answer.",
                'grammar_correct': False
            }
        
        # Clean the answer
        cleaned_answer = user_answer.strip()
        
        # Validate grammar
        grammar_result = validate_sentence(cleaned_answer)
        
        # Store validation history
        self.validation_history.append({
            'answer': cleaned_answer,
            'is_valid': grammar_result['is_valid'],
            'errors': grammar_result['errors']
        })
        
        if grammar_result['is_valid']:
            return {
                'is_valid': True,
                'score': 100,
                'feedback': f"✅ Excellent! '{cleaned_answer}' has correct grammar.",
                'grammar_correct': True,
                'details': grammar_result
            }
        else:
            # Provide constructive feedback
            feedback = f"❌ Grammar error detected in: '{cleaned_answer}'\n\n"
            feedback += "💡 Issues to fix:\n"
            
            for error in grammar_result['errors']:
                if 'message' in error:
                    feedback += f"  • {error['message']}\n"
            
            feedback += "\n🔧 Try to check:\n"
            feedback += "  • Subject-verb agreement (he/she/it + verb+s)\n"
            feedback += "  • Correct verb tense\n"
            feedback += "  • Proper sentence structure\n"
            
            return {
                'is_valid': False,
                'score': 0,
                'feedback': feedback.strip(),
                'grammar_correct': False,
                'details': grammar_result
            }
    
    def get_validation_stats(self):
        """
        Returns statistics about validation history
        """
        if not self.validation_history:
            return {'total': 0, 'correct': 0, 'accuracy': 0}
        
        total = len(self.validation_history)
        correct = sum(1 for v in self.validation_history if v['is_valid'])
        accuracy = (correct / total) * 100
        
        return {
            'total': total,
            'correct': correct,
            'incorrect': total - correct,
            'accuracy': round(accuracy, 2)
        }
    
    def provide_hint(self, incorrect_answer):
        """
        Provides hints for improving grammar in incorrect answers
        """
        # Analyze common grammar mistakes and provide specific hints
        lower_answer = incorrect_answer.lower()
        
        hints = []
        
        # Check for common subject-verb agreement issues
        if any(subj in lower_answer for subj in ['he ', 'she ', 'it ']):
            if any(verb in lower_answer for verb in [' go ', ' do ', ' have ', ' run ', ' walk ']):
                hints.append("💡 With 'he/she/it', use verbs ending in 's' (goes, does, has, runs, walks)")
        
        if any(subj in lower_answer for subj in ['they ', 'we ', 'i ', 'you ']):
            if any(verb in lower_answer for verb in [' goes ', ' does ', ' has ', ' runs ', ' walks ']):
                hints.append("💡 With 'they/we/I/you', use base form verbs (go, do, have, run, walk)")
        
        # Check for tense consistency
        if 'will ' in lower_answer and any(past in lower_answer for past in ['yesterday', 'last']):
            hints.append("💡 Don't use 'will' with past time expressions like 'yesterday'")
        
        if 'went' in lower_answer and any(future in lower_answer for future in ['tomorrow', 'next']):
            hints.append("💡 Don't use past tense 'went' with future time expressions")
        
        if not hints:
            hints.append("💡 Check subject-verb agreement and verb tenses")
        
        return hints


# Example usage and testing
if __name__ == "__main__":
    validator = AnswerValidator()
    
    # Test cases
    test_answers = [
        "I go to school every day",
        "She goes to the market",
        "She go to school",  # Incorrect
        "They are playing football",
        "He are happy",  # Incorrect
        "I will visit tomorrow",
        "I went yesterday",
        "I will went tomorrow"  # Incorrect
    ]
    
    print("Answer Validation Test Results:")
    print("=" * 60)
    
    for answer in test_answers:
        result = validator.validate_answer(answer)
        print(f"Answer: {answer}")
        print(f"Valid: {result['is_valid']}")
        print(f"Score: {result['score']}")
        print("Feedback:")
        print(result['feedback'])
        
        if not result['is_valid']:
            hints = validator.provide_hint(answer)
            print("\nHints:")
            for hint in hints:
                print(f"  {hint}")
        
        print("-" * 60)
    
    # Show validation statistics
    stats = validator.get_validation_stats()
    print(f"\nValidation Statistics:")
    print(f"Total answers: {stats['total']}")
    print(f"Correct: {stats['correct']}")
    print(f"Incorrect: {stats['incorrect']}")
    print(f"Accuracy: {stats['accuracy']}%")
