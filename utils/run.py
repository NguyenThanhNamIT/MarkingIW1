import sys, os
import subprocess
from antlr4 import *
from CompiledFiles.TenseQuizLexer import TenseQuizLexer
from CompiledFiles.TenseQuizParser import TenseQuizParser

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/antlr/antlr4-4.9.2-complete.jar' # your location is going here
CPL_Dest = 'CompiledFiles'
SRC = 'TenseQuiz.g4'
TESTS = os.path.join(DIR, './tests')

def printUsage():
    print('python run.py gen')
    print('python run.py test')

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
    tree = parser.answer()
    print(tree.toStringTree(recog=parser))

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()
    elif argv[0] == 'test':
        # Example 1: Full sentence
        prompt1 = "Write a past sentence using the verb 'go'."
        answer1 = "I went to the park yesterday"
        print(f"Prompt: {prompt1}")
        print(f"Answer: {answer1}")
        print("Parse Tree:")
        parse_answer(answer1)
        print("\n")

        # Example 2: Full sentence
        prompt2 = "Write a present sentence using the verb 'eat'."
        answer2 = "She eats a sandwich now"
        print(f"Prompt: {prompt2}")
        print(f"Answer: {answer2}")
        print("Parse Tree:")
        parse_answer(answer2)
        print("\n")

        # Example 3: Full sentence
        prompt3 = "Write a future sentence using the verb 'drive'."
        answer3 = "they will drive to school tomorrow"
        print(f"Prompt: {prompt3}")
        print(f"Answer: {answer3}")
        print("Parse Tree:")
        parse_answer(answer3)
        print("\n")

        # Example 4: Fill in the blank
        prompt4 = "Fill in the blank: He ___ (write) a letter tomorrow."
        answer4 = "will write"
        print(f"Prompt: {prompt4}")
        print(f"Answer: {answer4}")
        print("Parse Tree:")
        parse_answer(answer4)
    else:
        printUsage()

if __name__ == '__main__':
    main(sys.argv[1:])