import sys, os
import subprocess
from antlr4 import *

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = "C:/antlr/antlr4-4.9.2-complete.jar" # your location is going here
CPL_Dest = 'CompiledFiles'
SRC = 'TenseQuiz.g4'
TESTS = os.path.join(DIR, './tests')

def printUsage():
    print('python run.py gen')

def printBreak():
    print('-----------------------------------------------')

def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-visitor', '-Dlanguage=Python3', SRC])    
    print('Generate successfully')
    

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    else:
        printUsage()


if __name__ == '__main__':
    main(sys.argv[1:])     
    
    
    