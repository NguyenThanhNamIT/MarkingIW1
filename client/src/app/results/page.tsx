"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { API_BASE_URL } from "@/api/config";

interface DetailedResult {
    question_number: number;
    question: string;
    user_answer: string;
    is_correct: boolean;
    score: number;
    correct_answer: string[];
    verb_checks?: boolean[];
}

interface QuizResults {
    success: boolean;
    total_score: number;
    max_score: number;
    percentage: number;
    detailed_results: DetailedResult[];
}

export default function ResultsPage() {
    const [results, setResults] = useState<QuizResults | null>(null);
    const [loading, setLoading] = useState(true);
    const router = useRouter();

    useEffect(() => {
        fetchResults();
    }, []);

    const fetchResults = async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/results`, {
                credentials: "include",
            });

            if (response.ok) {
                const data = await response.json();
                setResults(data);
            } else {
                // No results found, redirect to home
                router.push("/");
            }
        } catch (error) {
            console.error("Error fetching results:", error);
            router.push("/");
        } finally {
            setLoading(false);
        }
    };

    const playAgain = async () => {
        try {
            await fetch(`${API_BASE_URL}/reset`, {
                method: "POST",
                credentials: "include",
            });
            router.push("/");
        } catch (error) {
            console.error("Error resetting game:", error);
            router.push("/");
        }
    };

    const getScoreColor = (percentage: number) => {
        if (percentage >= 80) return "text-green-600";
        if (percentage >= 60) return "text-yellow-600";
        if (percentage >= 40) return "text-orange-600";
        return "text-red-600";
    };

    const getScoreEmoji = (percentage: number) => {
        if (percentage >= 90) return "🏆";
        if (percentage >= 80) return "🎉";
        if (percentage >= 70) return "👏";
        if (percentage >= 60) return "👍";
        if (percentage >= 50) return "😊";
        return "📚";
    };

    const getScoreMessage = (percentage: number) => {
        if (percentage >= 90) return "Outstanding! Perfect grammar master!";
        if (percentage >= 80) return "Excellent work! You're a grammar star!";
        if (percentage >= 70) return "Great job! You have strong grammar skills!";
        if (percentage >= 60) return "Good work! Keep practicing to improve!";
        if (percentage >= 50) return "Not bad! You're on the right track!";
        return "Keep studying! Practice makes perfect!";
    };

    const getQuestionTypeIcon = (question: string) => {
        if (question.includes("Fill in the blank")) return "✏️";
        if (question.includes("Choose the correct")) return "🎯";
        if (question.includes("Complete the sentence")) return "🔗";
        if (question.includes("Correct the sentence")) return "🔧";
        return "❓";
    };

    const getQuestionTypeColor = (question: string) => {
        if (question.includes("Fill in the blank")) return "bg-blue-500";
        if (question.includes("Choose the correct")) return "bg-green-500";
        if (question.includes("Complete the sentence")) return "bg-purple-500";
        if (question.includes("Correct the sentence")) return "bg-orange-500";
        return "bg-gray-500";
    };

    if (loading) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-green-600 to-blue-600 flex items-center justify-center">
                <div className="text-white text-xl">Loading results...</div>
            </div>
        );
    }

    if (!results) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-red-600 to-pink-600 flex items-center justify-center">
                <div className="text-white text-xl">No results found</div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-green-600 to-blue-600 p-4">
            <div className="max-w-4xl mx-auto">
                {/* Header */}
                <div className="text-center mb-8">
                    <h1 className="text-5xl font-bold text-white mb-4">Quiz Complete!</h1>
                    <p className="text-xl text-white/90">Here are your results</p>
                </div>

                {/* Score Summary */}
                <div className="bg-white rounded-3xl shadow-2xl p-8 mb-8">
                    <div className="text-center">
                        <div className="text-8xl mb-4">{getScoreEmoji(results.percentage)}</div>
                        <div className={`text-6xl font-bold mb-4 ${getScoreColor(results.percentage)}`}>
                            {results.percentage}%
                        </div>
                        <h2 className="text-3xl font-bold text-gray-800 mb-2">
                            {getScoreMessage(results.percentage)}
                        </h2>
                        <p className="text-xl text-gray-600 mb-6">
                            You scored {results.total_score} out of {results.max_score} points
                        </p>

                        {/* Score Breakdown */}
                        <div className="grid grid-cols-3 gap-4 mb-8">
                            <div className="bg-blue-50 rounded-xl p-4">
                                <div className="text-2xl font-bold text-blue-600">{results.detailed_results.filter(r => r.is_correct).length}</div>
                                <div className="text-blue-800 font-medium">Correct</div>
                            </div>
                            <div className="bg-red-50 rounded-xl p-4">
                                <div className="text-2xl font-bold text-red-600">{results.detailed_results.filter(r => !r.is_correct).length}</div>
                                <div className="text-red-800 font-medium">Incorrect</div>
                            </div>
                            <div className="bg-purple-50 rounded-xl p-4">
                                <div className="text-2xl font-bold text-purple-600">{results.detailed_results.length}</div>
                                <div className="text-purple-800 font-medium">Total</div>
                            </div>
                        </div>

                        <button
                            onClick={playAgain}
                            className="bg-gradient-to-r from-green-600 to-blue-600 text-white text-xl font-bold py-4 px-12 rounded-2xl hover:from-green-700 hover:to-blue-700 transform hover:scale-105 transition-all duration-300 shadow-lg"
                        >
                            Play Again 🚀
                        </button>
                    </div>
                </div>

                {/* Detailed Results */}
                <div className="space-y-4">
                    <h3 className="text-2xl font-bold text-white mb-4">Detailed Review</h3>
                    {results.detailed_results.map((result, index) => (
                        <div key={index} className="bg-white rounded-2xl shadow-lg p-6">
                            <div className="flex items-start gap-4">
                                {/* Question Type Icon */}
                                <div className={`w-12 h-12 ${getQuestionTypeColor(result.question)} rounded-xl flex items-center justify-center text-white text-xl flex-shrink-0`}>
                                    {getQuestionTypeIcon(result.question)}
                                </div>

                                <div className="flex-1">
                                    {/* Question Header */}
                                    <div className="flex items-center justify-between mb-3">
                                        <h4 className="font-bold text-lg text-gray-800">
                                            Question {result.question_number}
                                        </h4>
                                        <div className={`px-4 py-2 rounded-full text-sm font-bold ${result.is_correct
                                            ? "bg-green-100 text-green-800"
                                            : "bg-red-100 text-red-800"
                                            }`}>
                                            {result.is_correct ? "✓ Correct" : "✗ Incorrect"} ({result.score}/{result.question.includes("Complete") ? "1" : "1"})
                                        </div>
                                    </div>

                                    {/* Question */}
                                    <p className="text-gray-700 mb-3 font-medium">{result.question}</p>

                                    {/* Answer Details */}
                                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                        <div>
                                            <p className="text-sm font-semibold text-gray-600 mb-1">Your Answer:</p>
                                            <p className={`font-medium ${result.is_correct ? "text-green-600" : "text-red-600"}`}>
                                                {result.user_answer}
                                            </p>
                                        </div>
                                        <div>
                                            <p className="text-sm font-semibold text-gray-600 mb-1">Correct Answer:</p>
                                            <p className="font-medium text-green-600">
                                                {Array.isArray(result.correct_answer)
                                                    ? result.correct_answer.join(", ")
                                                    : result.correct_answer}
                                            </p>
                                        </div>
                                    </div>

                                    {/* Verb Checks for Complete Questions */}
                                    {result.verb_checks && (
                                        <div className="mt-4 p-4 bg-gray-50 rounded-xl">
                                            <p className="text-sm font-semibold text-gray-600 mb-2">Verb Analysis:</p>
                                            <div className="grid grid-cols-2 gap-2">
                                                {result.verb_checks.map((isCorrect, verbIndex) => {
                                                    const userVerbs = result.user_answer.split(" and ");
                                                    const correctVerbs = result.correct_answer;
                                                    return (
                                                        <div key={verbIndex} className={`p-2 rounded text-sm ${isCorrect ? "bg-green-100 text-green-800" : "bg-red-100 text-red-800"
                                                            }`}>
                                                            <span className="font-semibold">Verb {verbIndex + 1}:</span> {userVerbs[verbIndex]}
                                                            {!isCorrect && (
                                                                <span className="block text-xs">Should be: {correctVerbs[verbIndex]}</span>
                                                            )}
                                                        </div>
                                                    );
                                                })}
                                            </div>
                                        </div>
                                    )}
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                {/* Footer */}
                <div className="text-center mt-8 pb-8">
                    <p className="text-white/70">Thanks for playing! Keep practicing to improve your grammar skills.</p>
                </div>
            </div>
        </div>
    );
}
