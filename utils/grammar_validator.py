"""
Grammar Validator Module
Provides simple functions to validate English grammar using ANTLR
"""

import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from .CompiledFiles.TenseQuizLexer import TenseQuizLexer
from .CompiledFiles.TenseQuizParser import TenseQuizParser


class GrammarErrorListener(ErrorListener):
    def __init__(self):
        super(GrammarErrorListener, self).__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            'line': line,
            'column': column,
            'message': msg,
            'symbol': str(offendingSymbol) if offendingSymbol else None
        })
    
    def has_errors(self):
        return len(self.errors) > 0
    
    def get_errors(self):
        return self.errors


def validate_sentence(sentence):
    """
    Validates if a sentence follows correct English grammar rules.
    
    Args:
        sentence (str): The sentence to validate
        
    Returns:
        dict: {
            'is_valid': bool,
            'errors': list,
            'parse_tree': str (if valid)
        }
    """
    try:
        input_stream = InputStream(sentence)
        lexer = TenseQuizLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = TenseQuizParser(stream)
        
        # Add error listener to catch parsing errors
        error_listener = GrammarErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        tree = parser.answer()
        
        if error_listener.has_errors():
            return {
                'is_valid': False,
                'errors': error_listener.get_errors(),
                'message': 'Grammar errors detected'
            }
        else:
            return {
                'is_valid': True,
                'errors': [],
                'parse_tree': tree.toStringTree(recog=parser),
                'message': 'Grammar is correct'
            }
            
    except Exception as e:
        return {
            'is_valid': False,
            'errors': [{'message': str(e)}],
            'message': f'Parsing failed: {str(e)}'
        }


def is_grammar_correct(sentence):
    """
    Simple function that returns True if grammar is correct, False otherwise.
    
    Args:
        sentence (str): The sentence to validate
        
    Returns:
        bool: True if grammar is correct, False otherwise
    """
    result = validate_sentence(sentence)
    return result['is_valid']


def get_grammar_errors(sentence):
    """
    Returns a list of grammar errors in the sentence.
    
    Args:
        sentence (str): The sentence to validate
        
    Returns:
        list: List of error dictionaries
    """
    result = validate_sentence(sentence)
    return result['errors']


def format_grammar_feedback(sentence):
    """
    Returns formatted feedback about the sentence's grammar.
    
    Args:
        sentence (str): The sentence to validate
        
    Returns:
        str: Formatted feedback message
    """
    result = validate_sentence(sentence)
    
    if result['is_valid']:
        return f"✅ Correct grammar: '{sentence}'"
    else:
        feedback = f"❌ Incorrect grammar: '{sentence}'\n"
        feedback += "Issues found:\n"
        for error in result['errors']:
            if 'line' in error and 'column' in error:
                feedback += f"  • Position {error['column']}: {error['message']}\n"
            else:
                feedback += f"  • {error['message']}\n"
        return feedback.strip()


# Example usage
if __name__ == "__main__":
    test_sentences = [
        "I go to school",
        "She goes to school", 
        "She go to school",  # Incorrect
        "They are happy",
        "He are happy",  # Incorrect
        "I will write a letter tomorrow",
        "I will wrote yesterday"  # Incorrect
    ]
    
    print("Grammar Validation Test Results:")
    print("=" * 50)
    
    for sentence in test_sentences:
        print(format_grammar_feedback(sentence))
        print()
