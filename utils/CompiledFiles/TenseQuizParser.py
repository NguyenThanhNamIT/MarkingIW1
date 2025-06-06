# Generated from TenseQuiz.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\f\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\2\2\4\2\4\2")
        buf.write("\3\3\2\3\5\2\t\2\6\3\2\2\2\4\t\3\2\2\2\6\7\5\4\3\2\7\b")
        buf.write("\7\2\2\3\b\3\3\2\2\2\t\n\t\2\2\2\n\5\3\2\2\2\2")
        return buf.getvalue()


class TenseQuizParser ( Parser ):

    grammarFileName = "TenseQuiz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PAST", "PRESENT", "FUTURE", "WS" ]

    RULE_answer = 0
    RULE_verb = 1

    ruleNames =  [ "answer", "verb" ]

    EOF = Token.EOF
    PAST=1
    PRESENT=2
    FUTURE=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AnswerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verb(self):
            return self.getTypedRuleContext(TenseQuizParser.VerbContext,0)


        def EOF(self):
            return self.getToken(TenseQuizParser.EOF, 0)

        def getRuleIndex(self):
            return TenseQuizParser.RULE_answer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnswer" ):
                return visitor.visitAnswer(self)
            else:
                return visitor.visitChildren(self)




    def answer(self):

        localctx = TenseQuizParser.AnswerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_answer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.verb()
            self.state = 5
            self.match(TenseQuizParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAST(self):
            return self.getToken(TenseQuizParser.PAST, 0)

        def PRESENT(self):
            return self.getToken(TenseQuizParser.PRESENT, 0)

        def FUTURE(self):
            return self.getToken(TenseQuizParser.FUTURE, 0)

        def getRuleIndex(self):
            return TenseQuizParser.RULE_verb

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb" ):
                return visitor.visitVerb(self)
            else:
                return visitor.visitChildren(self)




    def verb(self):

        localctx = TenseQuizParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_verb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TenseQuizParser.PAST) | (1 << TenseQuizParser.PRESENT) | (1 << TenseQuizParser.FUTURE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





