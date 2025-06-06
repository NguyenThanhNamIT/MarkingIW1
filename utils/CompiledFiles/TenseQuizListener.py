from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TenseQuizParser import TenseQuizParser
else:
    from TenseQuizParser import TenseQuizParser

class TenseQuizListener(ParseTreeListener):
    def __init__(self):
        self.tense = None

    def enterVerb(self, ctx:TenseQuizParser.VerbContext):
        if ctx.PAST():
            self.tense = "past"
        elif ctx.PRESENT():
            self.tense = "present"
        elif ctx.FUTURE():
            self.tense = "future"

    def get_tense(self):
        return self.tense

del TenseQuizParser