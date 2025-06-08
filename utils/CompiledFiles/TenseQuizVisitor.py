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


    # Visit a parse tree produced by TenseQuizParser#fill_in_the_blank.
    def visitFill_in_the_blank(self, ctx:TenseQuizParser.Fill_in_the_blankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#correct_sentence.
    def visitCorrect_sentence(self, ctx:TenseQuizParser.Correct_sentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#subject_verb_pair.
    def visitSubject_verb_pair(self, ctx:TenseQuizParser.Subject_verb_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#third_person_singular.
    def visitThird_person_singular(self, ctx:TenseQuizParser.Third_person_singularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#non_third_person.
    def visitNon_third_person(self, ctx:TenseQuizParser.Non_third_personContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#any_subject.
    def visitAny_subject(self, ctx:TenseQuizParser.Any_subjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#singular_noun_phrase.
    def visitSingular_noun_phrase(self, ctx:TenseQuizParser.Singular_noun_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#plural_noun_phrase.
    def visitPlural_noun_phrase(self, ctx:TenseQuizParser.Plural_noun_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#third_person_verb.
    def visitThird_person_verb(self, ctx:TenseQuizParser.Third_person_verbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#non_third_person_verb.
    def visitNon_third_person_verb(self, ctx:TenseQuizParser.Non_third_person_verbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#past_or_future_verb.
    def visitPast_or_future_verb(self, ctx:TenseQuizParser.Past_or_future_verbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#verb.
    def visitVerb(self, ctx:TenseQuizParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#direct_object.
    def visitDirect_object(self, ctx:TenseQuizParser.Direct_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#optional_content.
    def visitOptional_content(self, ctx:TenseQuizParser.Optional_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#prepositional_phrase.
    def visitPrepositional_phrase(self, ctx:TenseQuizParser.Prepositional_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#expression.
    def visitExpression(self, ctx:TenseQuizParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TenseQuizParser#noun_phrase.
    def visitNoun_phrase(self, ctx:TenseQuizParser.Noun_phraseContext):
        return self.visitChildren(ctx)



del TenseQuizParser