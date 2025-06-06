# Generated from TenseQuiz.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TenseQuizParser import TenseQuizParser
else:
    from TenseQuizParser import TenseQuizParser

# This class defines a complete generic visitor for a parse tree produced by TenseQuizParser.

class TenseQuizVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TenseQuizParser#answer.
    def visitAnswer(self, ctx:TenseQuizParser.AnswerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#verb.
    def visitVerb(self, ctx:TenseQuizParser.VerbContext):
        return self.visitChildren(ctx)



del TenseQuizParser