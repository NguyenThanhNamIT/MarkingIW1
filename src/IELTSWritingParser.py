# Generated from IELTSWriting.g4 by ANTLR 4.9.2
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
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3\35\n\3\3\4\3\4\3\4\5\4\"\n\4\3\4\3\4\7\4&\n")
        buf.write("\4\f\4\16\4)\13\4\3\4\3\4\3\5\3\5\3\5\5\5\60\n\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5\66\n\5\3\5\7\59\n\5\f\5\16\5<\13\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\5\6C\n\6\3\6\7\6F\n\6\f\6\16\6I\13\6")
        buf.write("\3\6\3\6\3\6\7\6N\n\6\f\6\16\6Q\13\6\3\6\3\6\3\7\3\7\7")
        buf.write("\7W\n\7\f\7\16\7Z\13\7\3\7\3\7\3\b\6\b_\n\b\r\b\16\b`")
        buf.write("\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\7\5\2\7\7\t\13\r\r")
        buf.write("\4\2\t\13\r\r\4\2\t\t\r\r\4\2\7\n\r\r\4\2\4\13\r\r\2l")
        buf.write("\2\21\3\2\2\2\4\34\3\2\2\2\6!\3\2\2\2\b/\3\2\2\2\nB\3")
        buf.write("\2\2\2\fT\3\2\2\2\16^\3\2\2\2\20\22\5\4\3\2\21\20\3\2")
        buf.write("\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\25\3")
        buf.write("\2\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\35\5\6\4\2\30\35")
        buf.write("\5\b\5\2\31\35\5\n\6\2\32\35\5\f\7\2\33\35\5\16\b\2\34")
        buf.write("\27\3\2\2\2\34\30\3\2\2\2\34\31\3\2\2\2\34\32\3\2\2\2")
        buf.write("\34\33\3\2\2\2\35\5\3\2\2\2\36\"\7\4\2\2\37 \7\5\2\2 ")
        buf.write("\"\7\4\2\2!\36\3\2\2\2!\37\3\2\2\2\"#\3\2\2\2#\'\7\6\2")
        buf.write("\2$&\t\2\2\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2")
        buf.write("(*\3\2\2\2)\'\3\2\2\2*+\7\f\2\2+\7\3\2\2\2,\60\7\4\2\2")
        buf.write("-.\7\5\2\2.\60\7\4\2\2/,\3\2\2\2/-\3\2\2\2\60\61\3\2\2")
        buf.write("\2\61\65\7\b\2\2\62\66\7\4\2\2\63\64\7\5\2\2\64\66\7\4")
        buf.write("\2\2\65\62\3\2\2\2\65\63\3\2\2\2\66:\3\2\2\2\679\t\3\2")
        buf.write("\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2\2\2")
        buf.write("<:\3\2\2\2=>\7\f\2\2>\t\3\2\2\2?C\7\4\2\2@A\7\5\2\2AC")
        buf.write("\7\4\2\2B?\3\2\2\2B@\3\2\2\2CG\3\2\2\2DF\t\4\2\2ED\3\2")
        buf.write("\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3\2\2\2")
        buf.write("JK\7\n\2\2KO\7\13\2\2LN\t\5\2\2ML\3\2\2\2NQ\3\2\2\2OM")
        buf.write("\3\2\2\2OP\3\2\2\2PR\3\2\2\2QO\3\2\2\2RS\7\f\2\2S\13\3")
        buf.write("\2\2\2TX\7\3\2\2UW\t\6\2\2VU\3\2\2\2WZ\3\2\2\2XV\3\2\2")
        buf.write("\2XY\3\2\2\2Y[\3\2\2\2ZX\3\2\2\2[\\\7\f\2\2\\\r\3\2\2")
        buf.write("\2]_\t\6\2\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2a")
        buf.write("b\3\2\2\2bc\7\f\2\2c\17\3\2\2\2\16\23\34!\'/\65:BGOX`")
        return buf.getvalue()


class IELTSWritingParser ( Parser ):

    grammarFileName = "IELTSWriting.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Overall'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NOUN", "ADJ", "VERB", "ADVERB", 
                      "COMPARE", "PREP", "NUMBER", "UNIT", "PUNCT", "WORD", 
                      "WS" ]

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
    NOUN=2
    ADJ=3
    VERB=4
    ADVERB=5
    COMPARE=6
    PREP=7
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.T__0) | (1 << IELTSWritingParser.NOUN) | (1 << IELTSWritingParser.ADJ) | (1 << IELTSWritingParser.VERB) | (1 << IELTSWritingParser.ADVERB) | (1 << IELTSWritingParser.COMPARE) | (1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.UNIT) | (1 << IELTSWritingParser.WORD))) != 0)):
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

        def VERB(self):
            return self.getToken(IELTSWritingParser.VERB, 0)

        def PUNCT(self):
            return self.getToken(IELTSWritingParser.PUNCT, 0)

        def NOUN(self):
            return self.getToken(IELTSWritingParser.NOUN, 0)

        def ADJ(self):
            return self.getToken(IELTSWritingParser.ADJ, 0)

        def ADVERB(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.ADVERB)
            else:
                return self.getToken(IELTSWritingParser.ADVERB, i)

        def PREP(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.PREP)
            else:
                return self.getToken(IELTSWritingParser.PREP, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.NUMBER)
            else:
                return self.getToken(IELTSWritingParser.NUMBER, i)

        def UNIT(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.UNIT)
            else:
                return self.getToken(IELTSWritingParser.UNIT, i)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.WORD)
            else:
                return self.getToken(IELTSWritingParser.WORD, i)

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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IELTSWritingParser.NOUN]:
                self.state = 28
                self.match(IELTSWritingParser.NOUN)
                pass
            elif token in [IELTSWritingParser.ADJ]:
                self.state = 29
                self.match(IELTSWritingParser.ADJ)
                self.state = 30
                self.match(IELTSWritingParser.NOUN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 33
            self.match(IELTSWritingParser.VERB)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.ADVERB) | (1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.UNIT) | (1 << IELTSWritingParser.WORD))) != 0):
                self.state = 34
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.ADVERB) | (1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.UNIT) | (1 << IELTSWritingParser.WORD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
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

        def COMPARE(self):
            return self.getToken(IELTSWritingParser.COMPARE, 0)

        def PUNCT(self):
            return self.getToken(IELTSWritingParser.PUNCT, 0)

        def NOUN(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.NOUN)
            else:
                return self.getToken(IELTSWritingParser.NOUN, i)

        def ADJ(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.ADJ)
            else:
                return self.getToken(IELTSWritingParser.ADJ, i)

        def PREP(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.PREP)
            else:
                return self.getToken(IELTSWritingParser.PREP, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.NUMBER)
            else:
                return self.getToken(IELTSWritingParser.NUMBER, i)

        def UNIT(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.UNIT)
            else:
                return self.getToken(IELTSWritingParser.UNIT, i)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.WORD)
            else:
                return self.getToken(IELTSWritingParser.WORD, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IELTSWritingParser.NOUN]:
                self.state = 42
                self.match(IELTSWritingParser.NOUN)
                pass
            elif token in [IELTSWritingParser.ADJ]:
                self.state = 43
                self.match(IELTSWritingParser.ADJ)
                self.state = 44
                self.match(IELTSWritingParser.NOUN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 47
            self.match(IELTSWritingParser.COMPARE)
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IELTSWritingParser.NOUN]:
                self.state = 48
                self.match(IELTSWritingParser.NOUN)
                pass
            elif token in [IELTSWritingParser.ADJ]:
                self.state = 49
                self.match(IELTSWritingParser.ADJ)
                self.state = 50
                self.match(IELTSWritingParser.NOUN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.UNIT) | (1 << IELTSWritingParser.WORD))) != 0):
                self.state = 53
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.UNIT) | (1 << IELTSWritingParser.WORD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
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

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.NUMBER)
            else:
                return self.getToken(IELTSWritingParser.NUMBER, i)

        def UNIT(self):
            return self.getToken(IELTSWritingParser.UNIT, 0)

        def PUNCT(self):
            return self.getToken(IELTSWritingParser.PUNCT, 0)

        def NOUN(self):
            return self.getToken(IELTSWritingParser.NOUN, 0)

        def ADJ(self):
            return self.getToken(IELTSWritingParser.ADJ, 0)

        def PREP(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.PREP)
            else:
                return self.getToken(IELTSWritingParser.PREP, i)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.WORD)
            else:
                return self.getToken(IELTSWritingParser.WORD, i)

        def ADVERB(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.ADVERB)
            else:
                return self.getToken(IELTSWritingParser.ADVERB, i)

        def COMPARE(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.COMPARE)
            else:
                return self.getToken(IELTSWritingParser.COMPARE, i)

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
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IELTSWritingParser.NOUN]:
                self.state = 61
                self.match(IELTSWritingParser.NOUN)
                pass
            elif token in [IELTSWritingParser.ADJ]:
                self.state = 62
                self.match(IELTSWritingParser.ADJ)
                self.state = 63
                self.match(IELTSWritingParser.NOUN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IELTSWritingParser.PREP or _la==IELTSWritingParser.WORD:
                self.state = 66
                _la = self._input.LA(1)
                if not(_la==IELTSWritingParser.PREP or _la==IELTSWritingParser.WORD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(IELTSWritingParser.NUMBER)
            self.state = 73
            self.match(IELTSWritingParser.UNIT)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.ADVERB) | (1 << IELTSWritingParser.COMPARE) | (1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.WORD))) != 0):
                self.state = 74
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.ADVERB) | (1 << IELTSWritingParser.COMPARE) | (1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.WORD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
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

        def NOUN(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.NOUN)
            else:
                return self.getToken(IELTSWritingParser.NOUN, i)

        def ADJ(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.ADJ)
            else:
                return self.getToken(IELTSWritingParser.ADJ, i)

        def VERB(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.VERB)
            else:
                return self.getToken(IELTSWritingParser.VERB, i)

        def ADVERB(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.ADVERB)
            else:
                return self.getToken(IELTSWritingParser.ADVERB, i)

        def PREP(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.PREP)
            else:
                return self.getToken(IELTSWritingParser.PREP, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.NUMBER)
            else:
                return self.getToken(IELTSWritingParser.NUMBER, i)

        def COMPARE(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.COMPARE)
            else:
                return self.getToken(IELTSWritingParser.COMPARE, i)

        def UNIT(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.UNIT)
            else:
                return self.getToken(IELTSWritingParser.UNIT, i)

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
            self.state = 82
            self.match(IELTSWritingParser.T__0)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.NOUN) | (1 << IELTSWritingParser.ADJ) | (1 << IELTSWritingParser.VERB) | (1 << IELTSWritingParser.ADVERB) | (1 << IELTSWritingParser.COMPARE) | (1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.UNIT) | (1 << IELTSWritingParser.WORD))) != 0):
                self.state = 83
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.NOUN) | (1 << IELTSWritingParser.ADJ) | (1 << IELTSWritingParser.VERB) | (1 << IELTSWritingParser.ADVERB) | (1 << IELTSWritingParser.COMPARE) | (1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.UNIT) | (1 << IELTSWritingParser.WORD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
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

        def NOUN(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.NOUN)
            else:
                return self.getToken(IELTSWritingParser.NOUN, i)

        def ADJ(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.ADJ)
            else:
                return self.getToken(IELTSWritingParser.ADJ, i)

        def VERB(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.VERB)
            else:
                return self.getToken(IELTSWritingParser.VERB, i)

        def ADVERB(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.ADVERB)
            else:
                return self.getToken(IELTSWritingParser.ADVERB, i)

        def PREP(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.PREP)
            else:
                return self.getToken(IELTSWritingParser.PREP, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.NUMBER)
            else:
                return self.getToken(IELTSWritingParser.NUMBER, i)

        def COMPARE(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.COMPARE)
            else:
                return self.getToken(IELTSWritingParser.COMPARE, i)

        def UNIT(self, i:int=None):
            if i is None:
                return self.getTokens(IELTSWritingParser.UNIT)
            else:
                return self.getToken(IELTSWritingParser.UNIT, i)

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
            self.state = 92 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 91
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.NOUN) | (1 << IELTSWritingParser.ADJ) | (1 << IELTSWritingParser.VERB) | (1 << IELTSWritingParser.ADVERB) | (1 << IELTSWritingParser.COMPARE) | (1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.UNIT) | (1 << IELTSWritingParser.WORD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 94 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IELTSWritingParser.NOUN) | (1 << IELTSWritingParser.ADJ) | (1 << IELTSWritingParser.VERB) | (1 << IELTSWritingParser.ADVERB) | (1 << IELTSWritingParser.COMPARE) | (1 << IELTSWritingParser.PREP) | (1 << IELTSWritingParser.NUMBER) | (1 << IELTSWritingParser.UNIT) | (1 << IELTSWritingParser.WORD))) != 0)):
                    break

            self.state = 96
            self.match(IELTSWritingParser.PUNCT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx











