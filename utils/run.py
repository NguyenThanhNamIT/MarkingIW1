import sys, os
import subprocess
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CompiledFiles.TenseQuizLexer import TenseQuizLexer
from CompiledFiles.TenseQuizParser import TenseQuizParser

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/antlr/antlr4-4.9.2-complete.jar' # your location is going here
CPL_Dest = 'CompiledFiles'
SRC = 'TenseQuiz.g4'
TESTS = os.path.join(DIR, './tests')

class GrammarErrorListener(ErrorListener):
    def __init__(self):
        super(GrammarErrorListener, self).__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Line {line}:{column} - {msg}")
    
    def has_errors(self):
        return len(self.errors) > 0
    
    def get_errors(self):
        return self.errors

def printUsage():
    print('python run.py gen          - Generate ANTLR parser files')
    print('python run.py test         - Run grammar validation tests')
    print('python run.py validate "sentence" - Validate a specific sentence')

def printBreak():
    print('-----------------------------------------------')

def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-visitor', '-Dlanguage=Python3', SRC])    
    print('Generate successfully')
    

def parse_answer(answer):
    input_stream = InputStream(answer)
    lexer = TenseQuizLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TenseQuizParser(stream)
    
    # Add error listener to catch parsing errors
    error_listener = GrammarErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    try:
        tree = parser.answer()
        
        if error_listener.has_errors():
            print("❌ GRAMMAR ERRORS DETECTED:")
            for error in error_listener.get_errors():
                print(f"  • {error}")
            return False, tree
        else:
            print("✅ Grammar is CORRECT!")
            print(f"Parse Tree: {tree.toStringTree(recog=parser)}")
            return True, tree
            
    except Exception as e:
        print(f"❌ PARSING FAILED: {str(e)}")
        return False, None

def validate_grammar(sentence):
    is_valid, tree = parse_answer(sentence)
    return is_valid

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()
    elif argv[0] == 'test':
        print("=== TESTING CORRECT GRAMMAR ===\n")
        
        # Example 1: Correct past sentence
        prompt1 = "Write a past sentence using the verb 'go'."
        answer1 = "I went to the park yesterday"
        print(f"Prompt: {prompt1}")
        print(f"Answer: {answer1}")
        parse_answer(answer1)
        print("\n")

        # Example 2: Correct present sentence
        prompt2 = "Write a present sentence using the verb 'eat'."
        answer2 = "She eats a sandwich now"
        print(f"Prompt: {prompt2}")
        print(f"Answer: {answer2}")
        parse_answer(answer2)
        print("\n")

        # Example 3: Correct future sentence
        prompt3 = "Write a future sentence using the verb 'drive'."
        answer3 = "They will drive to school tomorrow"
        print(f"Prompt: {prompt3}")
        print(f"Answer: {answer3}")
        parse_answer(answer3)
        print("\n")

        # Example 4: Fill in the blank
        prompt4 = "Fill in the blank: He ___ (write) a letter tomorrow."
        answer4 = "will write"
        print(f"Prompt: {prompt4}")
        print(f"Answer: {answer4}")
        parse_answer(answer4)
        print("\n")
        
        print("=== TESTING INCORRECT GRAMMAR ===\n")
        
        # Example 5: Subject-verb disagreement
        prompt5 = "Incorrect: Subject-verb disagreement"
        answer5 = "She go to school"  # Should be "goes"
        print(f"Test: {prompt5}")
        print(f"Answer: {answer5}")
        parse_answer(answer5)
        print("\n")
        
        # Example 6: Wrong tense with time expression
        prompt6 = "Incorrect: Wrong tense with time expression"
        answer6 = "I will went yesterday"  # Mixed tenses
        print(f"Test: {prompt6}")
        print(f"Answer: {answer6}")
        parse_answer(answer6)
        print("\n")
        
        # Example 7: Plural subject with singular verb
        prompt7 = "Incorrect: Plural subject with singular verb"
        answer7 = "They eats lunch"  # Should be "eat"
        print(f"Test: {prompt7}")
        print(f"Answer: {answer7}")
        parse_answer(answer7)
        print("\n")
        
    elif argv[0] == 'validate':
        if len(argv) < 2:
            print("Usage: python run.py validate \"sentence to check\"")
        else:
            sentence = argv[1]
            print(f"Validating: {sentence}")
            is_valid = validate_grammar(sentence)
            if is_valid:
                print("✅ The sentence has correct grammar!")
            else:
                print("❌ The sentence contains grammar errors!")
    else:
        printUsage()

if __name__ == '__main__':
    main(sys.argv[1:])