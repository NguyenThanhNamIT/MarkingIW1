# Generated from src/IELTSWriting.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("C\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3\35\n\3\3\4\3\4\3\4\5\4\"\n\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\60\n\6\3\6\3\6")
        buf.write("\3\7\3\7\6\7\66\n\7\r\7\16\7\67\3\7\3\7\3\b\6\b=\n\b\r")
        buf.write("\b\16\b>\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2D\2\21")
        buf.write("\3\2\2\2\4\34\3\2\2\2\6\36\3\2\2\2\b%\3\2\2\2\n*\3\2\2")
        buf.write("\2\f\63\3\2\2\2\16<\3\2\2\2\20\22\5\4\3\2\21\20\3\2\2")
        buf.write("\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\25\3\2")
        buf.write("\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\35\5\6\4\2\30\35\5")
        buf.write("\b\5\2\31\35\5\n\6\2\32\35\5\f\7\2\33\35\5\16\b\2\34\27")
        buf.write("\3\2\2\2\34\30\3\2\2\2\34\31\3\2\2\2\34\32\3\2\2\2\34")
        buf.write("\33\3\2\2\2\35\5\3\2\2\2\36\37\7\5\2\2\37!\7\6\2\2 \"")
        buf.write("\7\7\2\2! \3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\7\f\2\2$\7")
        buf.write("\3\2\2\2%&\7\5\2\2&\'\7\b\2\2\'(\7\5\2\2()\7\f\2\2)\t")
        buf.write("\3\2\2\2*+\7\5\2\2+,\7\3\2\2,-\7\t\2\2-/\7\n\2\2.\60\7")
        buf.write("\13\2\2/.\3\2\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\62\7\f")
        buf.write("\2\2\62\13\3\2\2\2\63\65\7\4\2\2\64\66\7\r\2\2\65\64\3")
        buf.write("\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\289\3\2\2")
        buf.write("\29:\7\f\2\2:\r\3\2\2\2;=\7\r\2\2<;\3\2\2\2=>\3\2\2\2")
        buf.write("><\3\2\2\2>?\3\2\2\2?@\3\2\2\2@A\7\f\2\2A\17\3\2\2\2\b")
        buf.write("\23\34!/\67>")
        return buf.getvalue()


class IELTSWritingParser ( Parser ):

    grammarFileName = "IELTSWriting.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'in'", "'Overall'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NOUN", "VERB", 
                      "ADVERB", "COMPARE", "YEAR", "NUMBER", "UNIT", "PUNCT", 
                      "WORD", "WS" ]

    RULE_essay = 0
    RULE_sentence = 1
    RULE_trend = 2
    RULE_comparison = 3
    RULE_data = 4
    RULE_overview = 5
    RULE_other = 6

    ruleNames =  [ "essay", "sentence", "trend", "comparison", "data", "overview", 
                   "other" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NOUN=3
    VERB=4
    ADVERB=5
    COMPARE=6
    YEAR=7
    NUMBER=8
    UNIT=9
    PUNCT=10
    WORD=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EssayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(IELTSWritingParser.EOF, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IELTSWritingParser.SentenceContext)
            else:
                return self.getTypedRuleContext(IELTSWritingParser.SentenceContext,i)


        def getRuleIndex(self):
            return IELTSWritingParser.RULE_essay

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEssay" ):
                listener.enterEssay(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEssay" ):
                listener.exitEssay(self)




    def essay(self):

        localctx = IELTSWritingParser.EssayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_essay)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.sentence()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.T__1) | (1 << IELTSWritingParser.NOUN) | (1 << IELTSWritingParser.WORD))) != 0)):
                    break

            self.state = 19
            self.match(IELTSWritingParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trend(self):
            return self.getTypedRuleContext(IELTSWritingParser.TrendContext,0)


        def comparison(self):
            return self.getTypedRuleContext(IELTSWritingParser.ComparisonContext,0)


        def data(self):
            return self.getTypedRuleContext(IELTSWritingParser.DataContext,0)


        def overview(self):
            return self.getTypedRuleContext(IELTSWritingParser.OverviewContext,0)


        def other(self):
            return self.getTypedRuleContext(IELTSWritingParser.OtherContext,0)


        def getRuleIndex(self):
            return IELTSWritingParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)




    def sentence(self):

        localctx = IELTSWritingParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.trend()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.comparison()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.data()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.overview()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 25
                self.other()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOUN(self):
            return self.getToken(IELTSWritingParser.NOUN, 0)

        def VERB(self):
            return self.getToken(IELTSWritingParser.VERB, 0)

        def PUNCT(self):
            return self.getToken(IELTSWritingParser.PUNCT, 0)

        def ADVERB(self):
            return self.getToken(IELTSWritingParser.ADVERB, 0)

        def getRuleIndex(self):
            return IELTSWritingParser.RULE_trend

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrend" ):
                listener.enterTrend(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrend" ):
                listener.exitTrend(self)




    def trend(self):

        localctx = IELTSWritingParser.TrendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_trend)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(IELTSWritingParser.NOUN)
            self.state = 29
            self.match(IELTSWritingParser.VERB)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IELTSWritingParser.ADVERB:
                self.state = 30
                self.match(IELTSWritingParser.ADVERB)


            self.state = 33
            self.match(IELTSWritingParser.PUNCT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOUN(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.NOUN)
            else:
                return self.getToken(IELTSWritingParser.NOUN, i)

        def COMPARE(self):
            return self.getToken(IELTSWritingParser.COMPARE, 0)

        def PUNCT(self):
            return self.getToken(IELTSWritingParser.PUNCT, 0)

        def getRuleIndex(self):
            return IELTSWritingParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = IELTSWritingParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(IELTSWritingParser.NOUN)
            self.state = 36
            self.match(IELTSWritingParser.COMPARE)
            self.state = 37
            self.match(IELTSWritingParser.NOUN)
            self.state = 38
            self.match(IELTSWritingParser.PUNCT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOUN(self):
            return self.getToken(IELTSWritingParser.NOUN, 0)

        def YEAR(self):
            return self.getToken(IELTSWritingParser.YEAR, 0)

        def NUMBER(self):
            return self.getToken(IELTSWritingParser.NUMBER, 0)

        def PUNCT(self):
            return self.getToken(IELTSWritingParser.PUNCT, 0)

        def UNIT(self):
            return self.getToken(IELTSWritingParser.UNIT, 0)

        def getRuleIndex(self):
            return IELTSWritingParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)




    def data(self):

        localctx = IELTSWritingParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(IELTSWritingParser.NOUN)
            self.state = 41
            self.match(IELTSWritingParser.T__0)
            self.state = 42
            self.match(IELTSWritingParser.YEAR)
            self.state = 43
            self.match(IELTSWritingParser.NUMBER)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IELTSWritingParser.UNIT:
                self.state = 44
                self.match(IELTSWritingParser.UNIT)


            self.state = 47
            self.match(IELTSWritingParser.PUNCT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OverviewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNCT(self):
            return self.getToken(IELTSWritingParser.PUNCT, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.WORD)
            else:
                return self.getToken(IELTSWritingParser.WORD, i)

        def getRuleIndex(self):
            return IELTSWritingParser.RULE_overview

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOverview" ):
                listener.enterOverview(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOverview" ):
                listener.exitOverview(self)




    def overview(self):

        localctx = IELTSWritingParser.OverviewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_overview)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(IELTSWritingParser.T__1)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.match(IELTSWritingParser.WORD)
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IELTSWritingParser.WORD):
                    break

            self.state = 55
            self.match(IELTSWritingParser.PUNCT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNCT(self):
            return self.getToken(IELTSWritingParser.PUNCT, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.WORD)
            else:
                return self.getToken(IELTSWritingParser.WORD, i)

        def getRuleIndex(self):
            return IELTSWritingParser.RULE_other

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther" ):
                listener.enterOther(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther" ):
                listener.exitOther(self)




    def other(self):

        localctx = IELTSWritingParser.OtherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_other)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.match(IELTSWritingParser.WORD)
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IELTSWritingParser.WORD):
                    break

            self.state = 62
            self.match(IELTSWritingParser.PUNCT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





