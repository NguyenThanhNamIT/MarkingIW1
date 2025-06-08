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
        elif ctx.THIRD_PERSON_PRESENT() or ctx.NON_THIRD_PERSON_PRESENT() or ctx.BE_PRESENT():
            self.tense = "present"
        elif ctx.FUTURE():
            self.tense = "future"
        elif ctx.BE_PAST():
            self.tense = "past"

    def get_tense(self):
        return self.tense

del TenseQuizParser