// Generated from f:/MarkingIW1-main/MarkingIW1-main/src/IELTSWriting.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class IELTSWritingParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, NOUN=2, ADJ=3, VERB=4, ADVERB=5, COMPARE=6, PREP=7, NUMBER=8, 
		UNIT=9, PUNCT=10, WORD=11, WS=12;
	public static final int
		RULE_essay = 0, RULE_sentence = 1, RULE_trend = 2, RULE_comparison = 3, 
		RULE_data = 4, RULE_overview = 5, RULE_other = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"essay", "sentence", "trend", "comparison", "data", "overview", "other"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Overall'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "NOUN", "ADJ", "VERB", "ADVERB", "COMPARE", "PREP", "NUMBER", 
			"UNIT", "PUNCT", "WORD", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "IELTSWriting.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public IELTSWritingParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EssayContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(IELTSWritingParser.EOF, 0); }
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
		}
		public EssayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_essay; }
	}

	public final EssayContext essay() throws RecognitionException {
		EssayContext _localctx = new EssayContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_essay);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(15); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(14);
				sentence();
				}
				}
				setState(17); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 3070L) != 0) );
			setState(19);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenceContext extends ParserRuleContext {
		public TrendContext trend() {
			return getRuleContext(TrendContext.class,0);
		}
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public DataContext data() {
			return getRuleContext(DataContext.class,0);
		}
		public OverviewContext overview() {
			return getRuleContext(OverviewContext.class,0);
		}
		public OtherContext other() {
			return getRuleContext(OtherContext.class,0);
		}
		public SentenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentence; }
	}

	public final SentenceContext sentence() throws RecognitionException {
		SentenceContext _localctx = new SentenceContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sentence);
		try {
			setState(26);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(21);
				trend();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(22);
				comparison();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(23);
				data();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(24);
				overview();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(25);
				other();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TrendContext extends ParserRuleContext {
		public TerminalNode VERB() { return getToken(IELTSWritingParser.VERB, 0); }
		public TerminalNode PUNCT() { return getToken(IELTSWritingParser.PUNCT, 0); }
		public TerminalNode NOUN() { return getToken(IELTSWritingParser.NOUN, 0); }
		public TerminalNode ADJ() { return getToken(IELTSWritingParser.ADJ, 0); }
		public List<TerminalNode> ADVERB() { return getTokens(IELTSWritingParser.ADVERB); }
		public TerminalNode ADVERB(int i) {
			return getToken(IELTSWritingParser.ADVERB, i);
		}
		public List<TerminalNode> PREP() { return getTokens(IELTSWritingParser.PREP); }
		public TerminalNode PREP(int i) {
			return getToken(IELTSWritingParser.PREP, i);
		}
		public List<TerminalNode> NUMBER() { return getTokens(IELTSWritingParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(IELTSWritingParser.NUMBER, i);
		}
		public List<TerminalNode> UNIT() { return getTokens(IELTSWritingParser.UNIT); }
		public TerminalNode UNIT(int i) {
			return getToken(IELTSWritingParser.UNIT, i);
		}
		public List<TerminalNode> WORD() { return getTokens(IELTSWritingParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(IELTSWritingParser.WORD, i);
		}
		public TrendContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_trend; }
	}

	public final TrendContext trend() throws RecognitionException {
		TrendContext _localctx = new TrendContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_trend);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOUN:
				{
				setState(28);
				match(NOUN);
				}
				break;
			case ADJ:
				{
				setState(29);
				match(ADJ);
				setState(30);
				match(NOUN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(33);
			match(VERB);
			setState(37);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2976L) != 0)) {
				{
				{
				setState(34);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2976L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(39);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(40);
			match(PUNCT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonContext extends ParserRuleContext {
		public TerminalNode COMPARE() { return getToken(IELTSWritingParser.COMPARE, 0); }
		public TerminalNode PUNCT() { return getToken(IELTSWritingParser.PUNCT, 0); }
		public List<TerminalNode> NOUN() { return getTokens(IELTSWritingParser.NOUN); }
		public TerminalNode NOUN(int i) {
			return getToken(IELTSWritingParser.NOUN, i);
		}
		public List<TerminalNode> ADJ() { return getTokens(IELTSWritingParser.ADJ); }
		public TerminalNode ADJ(int i) {
			return getToken(IELTSWritingParser.ADJ, i);
		}
		public List<TerminalNode> PREP() { return getTokens(IELTSWritingParser.PREP); }
		public TerminalNode PREP(int i) {
			return getToken(IELTSWritingParser.PREP, i);
		}
		public List<TerminalNode> NUMBER() { return getTokens(IELTSWritingParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(IELTSWritingParser.NUMBER, i);
		}
		public List<TerminalNode> UNIT() { return getTokens(IELTSWritingParser.UNIT); }
		public TerminalNode UNIT(int i) {
			return getToken(IELTSWritingParser.UNIT, i);
		}
		public List<TerminalNode> WORD() { return getTokens(IELTSWritingParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(IELTSWritingParser.WORD, i);
		}
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOUN:
				{
				setState(42);
				match(NOUN);
				}
				break;
			case ADJ:
				{
				setState(43);
				match(ADJ);
				setState(44);
				match(NOUN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(47);
			match(COMPARE);
			setState(51);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOUN:
				{
				setState(48);
				match(NOUN);
				}
				break;
			case ADJ:
				{
				setState(49);
				match(ADJ);
				setState(50);
				match(NOUN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2944L) != 0)) {
				{
				{
				setState(53);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2944L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(59);
			match(PUNCT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DataContext extends ParserRuleContext {
		public List<TerminalNode> NUMBER() { return getTokens(IELTSWritingParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(IELTSWritingParser.NUMBER, i);
		}
		public TerminalNode UNIT() { return getToken(IELTSWritingParser.UNIT, 0); }
		public TerminalNode PUNCT() { return getToken(IELTSWritingParser.PUNCT, 0); }
		public TerminalNode NOUN() { return getToken(IELTSWritingParser.NOUN, 0); }
		public TerminalNode ADJ() { return getToken(IELTSWritingParser.ADJ, 0); }
		public List<TerminalNode> PREP() { return getTokens(IELTSWritingParser.PREP); }
		public TerminalNode PREP(int i) {
			return getToken(IELTSWritingParser.PREP, i);
		}
		public List<TerminalNode> WORD() { return getTokens(IELTSWritingParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(IELTSWritingParser.WORD, i);
		}
		public List<TerminalNode> ADVERB() { return getTokens(IELTSWritingParser.ADVERB); }
		public TerminalNode ADVERB(int i) {
			return getToken(IELTSWritingParser.ADVERB, i);
		}
		public List<TerminalNode> COMPARE() { return getTokens(IELTSWritingParser.COMPARE); }
		public TerminalNode COMPARE(int i) {
			return getToken(IELTSWritingParser.COMPARE, i);
		}
		public DataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_data; }
	}

	public final DataContext data() throws RecognitionException {
		DataContext _localctx = new DataContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_data);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOUN:
				{
				setState(61);
				match(NOUN);
				}
				break;
			case ADJ:
				{
				setState(62);
				match(ADJ);
				setState(63);
				match(NOUN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PREP || _la==WORD) {
				{
				{
				setState(66);
				_la = _input.LA(1);
				if ( !(_la==PREP || _la==WORD) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(72);
			match(NUMBER);
			setState(73);
			match(UNIT);
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2528L) != 0)) {
				{
				{
				setState(74);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2528L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(80);
			match(PUNCT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OverviewContext extends ParserRuleContext {
		public TerminalNode PUNCT() { return getToken(IELTSWritingParser.PUNCT, 0); }
		public List<TerminalNode> NOUN() { return getTokens(IELTSWritingParser.NOUN); }
		public TerminalNode NOUN(int i) {
			return getToken(IELTSWritingParser.NOUN, i);
		}
		public List<TerminalNode> ADJ() { return getTokens(IELTSWritingParser.ADJ); }
		public TerminalNode ADJ(int i) {
			return getToken(IELTSWritingParser.ADJ, i);
		}
		public List<TerminalNode> VERB() { return getTokens(IELTSWritingParser.VERB); }
		public TerminalNode VERB(int i) {
			return getToken(IELTSWritingParser.VERB, i);
		}
		public List<TerminalNode> ADVERB() { return getTokens(IELTSWritingParser.ADVERB); }
		public TerminalNode ADVERB(int i) {
			return getToken(IELTSWritingParser.ADVERB, i);
		}
		public List<TerminalNode> PREP() { return getTokens(IELTSWritingParser.PREP); }
		public TerminalNode PREP(int i) {
			return getToken(IELTSWritingParser.PREP, i);
		}
		public List<TerminalNode> NUMBER() { return getTokens(IELTSWritingParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(IELTSWritingParser.NUMBER, i);
		}
		public List<TerminalNode> COMPARE() { return getTokens(IELTSWritingParser.COMPARE); }
		public TerminalNode COMPARE(int i) {
			return getToken(IELTSWritingParser.COMPARE, i);
		}
		public List<TerminalNode> UNIT() { return getTokens(IELTSWritingParser.UNIT); }
		public TerminalNode UNIT(int i) {
			return getToken(IELTSWritingParser.UNIT, i);
		}
		public List<TerminalNode> WORD() { return getTokens(IELTSWritingParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(IELTSWritingParser.WORD, i);
		}
		public OverviewContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overview; }
	}

	public final OverviewContext overview() throws RecognitionException {
		OverviewContext _localctx = new OverviewContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_overview);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(T__0);
			setState(86);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3068L) != 0)) {
				{
				{
				setState(83);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3068L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(88);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(89);
			match(PUNCT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OtherContext extends ParserRuleContext {
		public TerminalNode PUNCT() { return getToken(IELTSWritingParser.PUNCT, 0); }
		public List<TerminalNode> NOUN() { return getTokens(IELTSWritingParser.NOUN); }
		public TerminalNode NOUN(int i) {
			return getToken(IELTSWritingParser.NOUN, i);
		}
		public List<TerminalNode> ADJ() { return getTokens(IELTSWritingParser.ADJ); }
		public TerminalNode ADJ(int i) {
			return getToken(IELTSWritingParser.ADJ, i);
		}
		public List<TerminalNode> VERB() { return getTokens(IELTSWritingParser.VERB); }
		public TerminalNode VERB(int i) {
			return getToken(IELTSWritingParser.VERB, i);
		}
		public List<TerminalNode> ADVERB() { return getTokens(IELTSWritingParser.ADVERB); }
		public TerminalNode ADVERB(int i) {
			return getToken(IELTSWritingParser.ADVERB, i);
		}
		public List<TerminalNode> PREP() { return getTokens(IELTSWritingParser.PREP); }
		public TerminalNode PREP(int i) {
			return getToken(IELTSWritingParser.PREP, i);
		}
		public List<TerminalNode> NUMBER() { return getTokens(IELTSWritingParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(IELTSWritingParser.NUMBER, i);
		}
		public List<TerminalNode> COMPARE() { return getTokens(IELTSWritingParser.COMPARE); }
		public TerminalNode COMPARE(int i) {
			return getToken(IELTSWritingParser.COMPARE, i);
		}
		public List<TerminalNode> UNIT() { return getTokens(IELTSWritingParser.UNIT); }
		public TerminalNode UNIT(int i) {
			return getToken(IELTSWritingParser.UNIT, i);
		}
		public List<TerminalNode> WORD() { return getTokens(IELTSWritingParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(IELTSWritingParser.WORD, i);
		}
		public OtherContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_other; }
	}

	public final OtherContext other() throws RecognitionException {
		OtherContext _localctx = new OtherContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_other);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(91);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3068L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(94); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 3068L) != 0) );
			setState(96);
			match(PUNCT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\fc\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000\u0004\u0000\u0010"+
		"\b\u0000\u000b\u0000\f\u0000\u0011\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u001b\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002 \b\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u0002$\b\u0002\n\u0002\f\u0002\'\t\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003.\b\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u00034\b\u0003"+
		"\u0001\u0003\u0005\u00037\b\u0003\n\u0003\f\u0003:\t\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004A\b\u0004"+
		"\u0001\u0004\u0005\u0004D\b\u0004\n\u0004\f\u0004G\t\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0005\u0004L\b\u0004\n\u0004\f\u0004O\t\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0005\u0005U\b\u0005"+
		"\n\u0005\f\u0005X\t\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0004\u0006"+
		"]\b\u0006\u000b\u0006\f\u0006^\u0001\u0006\u0001\u0006\u0001\u0006\u0000"+
		"\u0000\u0007\u0000\u0002\u0004\u0006\b\n\f\u0000\u0005\u0003\u0000\u0005"+
		"\u0005\u0007\t\u000b\u000b\u0002\u0000\u0007\t\u000b\u000b\u0002\u0000"+
		"\u0007\u0007\u000b\u000b\u0002\u0000\u0005\b\u000b\u000b\u0002\u0000\u0002"+
		"\t\u000b\u000bj\u0000\u000f\u0001\u0000\u0000\u0000\u0002\u001a\u0001"+
		"\u0000\u0000\u0000\u0004\u001f\u0001\u0000\u0000\u0000\u0006-\u0001\u0000"+
		"\u0000\u0000\b@\u0001\u0000\u0000\u0000\nR\u0001\u0000\u0000\u0000\f\\"+
		"\u0001\u0000\u0000\u0000\u000e\u0010\u0003\u0002\u0001\u0000\u000f\u000e"+
		"\u0001\u0000\u0000\u0000\u0010\u0011\u0001\u0000\u0000\u0000\u0011\u000f"+
		"\u0001\u0000\u0000\u0000\u0011\u0012\u0001\u0000\u0000\u0000\u0012\u0013"+
		"\u0001\u0000\u0000\u0000\u0013\u0014\u0005\u0000\u0000\u0001\u0014\u0001"+
		"\u0001\u0000\u0000\u0000\u0015\u001b\u0003\u0004\u0002\u0000\u0016\u001b"+
		"\u0003\u0006\u0003\u0000\u0017\u001b\u0003\b\u0004\u0000\u0018\u001b\u0003"+
		"\n\u0005\u0000\u0019\u001b\u0003\f\u0006\u0000\u001a\u0015\u0001\u0000"+
		"\u0000\u0000\u001a\u0016\u0001\u0000\u0000\u0000\u001a\u0017\u0001\u0000"+
		"\u0000\u0000\u001a\u0018\u0001\u0000\u0000\u0000\u001a\u0019\u0001\u0000"+
		"\u0000\u0000\u001b\u0003\u0001\u0000\u0000\u0000\u001c \u0005\u0002\u0000"+
		"\u0000\u001d\u001e\u0005\u0003\u0000\u0000\u001e \u0005\u0002\u0000\u0000"+
		"\u001f\u001c\u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000"+
		" !\u0001\u0000\u0000\u0000!%\u0005\u0004\u0000\u0000\"$\u0007\u0000\u0000"+
		"\u0000#\"\u0001\u0000\u0000\u0000$\'\u0001\u0000\u0000\u0000%#\u0001\u0000"+
		"\u0000\u0000%&\u0001\u0000\u0000\u0000&(\u0001\u0000\u0000\u0000\'%\u0001"+
		"\u0000\u0000\u0000()\u0005\n\u0000\u0000)\u0005\u0001\u0000\u0000\u0000"+
		"*.\u0005\u0002\u0000\u0000+,\u0005\u0003\u0000\u0000,.\u0005\u0002\u0000"+
		"\u0000-*\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000./\u0001\u0000"+
		"\u0000\u0000/3\u0005\u0006\u0000\u000004\u0005\u0002\u0000\u000012\u0005"+
		"\u0003\u0000\u000024\u0005\u0002\u0000\u000030\u0001\u0000\u0000\u0000"+
		"31\u0001\u0000\u0000\u000048\u0001\u0000\u0000\u000057\u0007\u0001\u0000"+
		"\u000065\u0001\u0000\u0000\u00007:\u0001\u0000\u0000\u000086\u0001\u0000"+
		"\u0000\u000089\u0001\u0000\u0000\u00009;\u0001\u0000\u0000\u0000:8\u0001"+
		"\u0000\u0000\u0000;<\u0005\n\u0000\u0000<\u0007\u0001\u0000\u0000\u0000"+
		"=A\u0005\u0002\u0000\u0000>?\u0005\u0003\u0000\u0000?A\u0005\u0002\u0000"+
		"\u0000@=\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000AE\u0001\u0000"+
		"\u0000\u0000BD\u0007\u0002\u0000\u0000CB\u0001\u0000\u0000\u0000DG\u0001"+
		"\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000"+
		"FH\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000HI\u0005\b\u0000\u0000"+
		"IM\u0005\t\u0000\u0000JL\u0007\u0003\u0000\u0000KJ\u0001\u0000\u0000\u0000"+
		"LO\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000"+
		"\u0000NP\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PQ\u0005\n\u0000"+
		"\u0000Q\t\u0001\u0000\u0000\u0000RV\u0005\u0001\u0000\u0000SU\u0007\u0004"+
		"\u0000\u0000TS\u0001\u0000\u0000\u0000UX\u0001\u0000\u0000\u0000VT\u0001"+
		"\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WY\u0001\u0000\u0000\u0000"+
		"XV\u0001\u0000\u0000\u0000YZ\u0005\n\u0000\u0000Z\u000b\u0001\u0000\u0000"+
		"\u0000[]\u0007\u0004\u0000\u0000\\[\u0001\u0000\u0000\u0000]^\u0001\u0000"+
		"\u0000\u0000^\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_`\u0001"+
		"\u0000\u0000\u0000`a\u0005\n\u0000\u0000a\r\u0001\u0000\u0000\u0000\f"+
		"\u0011\u001a\u001f%-38@EMV^";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}