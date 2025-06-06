// Generated from f:/TenseQuiz/TenseQuiz/TenseQuiz/src/TenseQuiz.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TenseQuizParser}.
 */
public interface TenseQuizListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TenseQuizParser#answer}.
	 * @param ctx the parse tree
	 */
	void enterAnswer(TenseQuizParser.AnswerContext ctx);
	/**
	 * Exit a parse tree produced by {@link TenseQuizParser#answer}.
	 * @param ctx the parse tree
	 */
	void exitAnswer(TenseQuizParser.AnswerContext ctx);
	/**
	 * Enter a parse tree produced by {@link TenseQuizParser#verb}.
	 * @param ctx the parse tree
	 */
	void enterVerb(TenseQuizParser.VerbContext ctx);
	/**
	 * Exit a parse tree produced by {@link TenseQuizParser#verb}.
	 * @param ctx the parse tree
	 */
	void exitVerb(TenseQuizParser.VerbContext ctx);
}