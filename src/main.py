from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from IELTSWritingLexer import IELTSWritingLexer
from IELTSWritingParser import IELTSWritingParser
import re

class SilentErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        pass
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

def score_text(writing, graph_description):
    word_count = len(writing.split())
    is_static_chart = "bar chart" in graph_description.lower() or "pie chart" in graph_description.lower()
    has_trend = bool(re.search(r'\bincreased\b|\bdecreased\b|\brose\b|\bfell\b|\bremained\b|\breached\b|\bachieved\b|\brecorded\b|\bpresents\b|\bstood\b|\bemphasizes\b|\breflects\b', writing, re.I)) if not is_static_chart else True
    has_comparison = bool(re.search(r'\bhigher than\b|\blower than\b|\bequal to\b|\bsimilar to\b|\bsurpassed\b|\bexceeded\b', writing, re.I))
    has_overview = bool(re.search(r'\bOverall\b', writing, re.I))
    has_abbreviations = bool(re.search(r'\bUSA\b|\bUK\b|\bEU\b', writing, re.I))

    ta = 5 + (1 if has_trend else 0) + (1 if has_comparison else 0)
    cc = 5 + (1 if has_overview else 0)
    lr = 5 + (1 if word_count >= 150 and not has_abbreviations else 0)
    gra = 5

    overall = (ta + cc + lr + gra) / 4
    if word_count < 150:
        overall = max(4.0, overall - 3.0)

    return min(ta, 9), min(cc, 9), min(lr, 9), min(gra, 9), has_trend, has_comparison, has_overview, word_count, overall, has_abbreviations

def main():
    print("Enter graph description:")
    graph = input().strip()
    
    print("Enter your writing as a single block (paragraphs separated by blank lines, press Enter twice to finish):")
    writing_lines = []
    while True:
        line = input()
        if line == "":
            break
        writing_lines.append(line.strip())
    writing = "\n".join(writing_lines)
    
    while True:
        print("Enter 'confirm' to start scoring (or 'exit' to quit):")
        confirmation = input().strip().lower()
        if confirmation == 'confirm':
            break
        elif confirmation == 'exit':
            print("Exiting program.")
            return
        else:
            print("Invalid input. Please enter 'confirm' to proceed or 'exit' to quit.")

    if not writing.strip():
        print("Error: No writing provided.")
        return

    # Normalize spaces
    writing = re.sub(r'\s+', ' ', writing)
    input_stream = InputStream(writing)
    lexer = IELTSWritingLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = IELTSWritingParser(stream)
    parser.removeErrorListeners()  # Remove default error listeners
    parser.addErrorListener(SilentErrorListener())  # Add silent listener
    parser.essay()  # Parse without output

    ta, cc, lr, gra, has_trend, has_comparison, has_overview, word_count, overall, has_abbreviations = score_text(writing, graph)
    print("\nBand Scores:")
    print(f"- Task Achievement: {ta}")
    print(f"- Coherence and Cohesion: {cc}")
    print(f"- Lexical Resource: {lr}")
    print(f"- Grammatical Range: {gra}")
    print(f"Overall: {overall:.1f}")
    suggestions = []
    is_static_chart = "bar chart" in graph.lower() or "pie chart" in graph.lower()
    if not is_static_chart and not has_trend:
        suggestions.append("Use verbs like 'increased', 'rose', 'remained', 'reached', 'achieved', 'recorded', or 'stood' to describe trends.")
    if not has_comparison:
        suggestions.append("Include comparisons like 'higher than', 'lower than', 'surpassed', or 'exceeded'.")
    if not has_overview:
        suggestions.append("Start a sentence with 'Overall' to summarize the data.")
    if word_count < 150:
        suggestions.append(f"Write more (current: {word_count} words; aim for 150+).")
    if has_abbreviations:
        suggestions.append("Use full words instead of abbreviations (e.g., 'United States' instead of 'USA').")
    print("Suggestions:", "; ".join(suggestions) if suggestions else "Good job!")

if __name__ == '__main__':
    main()
