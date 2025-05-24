from antlr4 import *
from IELTSWritingLexer import IELTSWritingLexer
from IELTSWritingParser import IELTSWritingParser
import re

def score_text(writing):
    word_count = len(writing.split())
    has_trend = bool(re.search(r'\bincreased\b|\bdecreased\b|\brose\b|\bfell\b', writing, re.I))
    has_comparison = bool(re.search(r'\bhigher than\b|\blower than\b', writing, re.I))
    has_overview = bool(re.search(r'\bOverall\b', writing, re.I))

    ta = 5 + (1 if has_trend else 0) + (1 if has_comparison else 0)
    cc = 5 + (1 if has_overview else 0)
    lr = 5 + (1 if word_count > 50 else 0)
    gra = 5

    return min(ta, 9), min(cc, 9), min(lr, 9), min(gra, 9), has_trend, has_comparison, has_overview, word_count

def main():
    graph = input("Enter graph description: ")
    writing = input("Enter your writing: ")
    input_stream = InputStream(writing)
    lexer = IELTSWritingLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = IELTSWritingParser(stream)
    tree = parser.essay()
    print("Parse tree:", tree.toStringTree(recog=parser))

    ta, cc, lr, gra, has_trend, has_comparison, has_overview, word_count = score_text(writing)
    overall = (ta + cc + lr + gra) / 4
    print("\nBand Scores:")
    print(f"- Task Achievement: {ta}")
    print(f"- Coherence and Cohesion: {cc}")
    print(f"- Lexical Resource: {lr}")
    print(f"- Grammatical Range: {gra}")
    print(f"Overall: {overall:.1f}")
    suggestions = []
    if not has_trend: suggestions.append("Add trends (e.g., 'increased').")
    if not has_comparison: suggestions.append("Add comparisons (e.g., 'higher than').")
    if not has_overview: suggestions.append("Add an overview (e.g., 'Overall sales rose').")
    if word_count < 50: suggestions.append("Write more (aim for 150+ words).")
    print("Suggestions:", "; ".join(suggestions) if suggestions else "Good job!")

if __name__ == '__main__':
    main()
