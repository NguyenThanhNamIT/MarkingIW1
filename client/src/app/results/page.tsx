"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { API_BASE_URL } from "@/api/config";

interface AnswerHistory {
    question: {
        id: string;
        type: string;
        prompt: string;
    };
    user_answer: string;
    is_correct: boolean;
    feedback: string;
}

interface QuizResults {
    success: boolean;
    results: {
        score: number;
        total_questions: number;
        accuracy: number;
        answers_history: AnswerHistory[];
    };
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
    }; const playAgain = async () => {
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
    }; const getScoreColor = (accuracy: number) => {
        if (accuracy >= 80) return "text-green-600";
        if (accuracy >= 60) return "text-yellow-600";
        if (accuracy >= 40) return "text-orange-600";
        return "text-red-600";
    };

    const getScoreEmoji = (accuracy: number) => {
        if (accuracy >= 90) return "🏆";
        if (accuracy >= 80) return "🎉";
        if (accuracy >= 70) return "👏";
        if (accuracy >= 60) return "👍";
        if (accuracy >= 50) return "😊";
        return "📚";
    };

    const getScoreMessage = (accuracy: number) => {
        if (accuracy >= 90) return "Outstanding! Perfect grammar master!";
        if (accuracy >= 80) return "Excellent work! You're a grammar star!";
        if (accuracy >= 70) return "Great job! You have strong grammar skills!";
        if (accuracy >= 60) return "Good work! Keep practicing to improve!";
        if (accuracy >= 50) return "Not bad! You're on the right track!";
        return "Keep studying! Practice makes perfect!";
    };

    const getQuestionTypeIcon = (type: string) => {
        switch (type) {
            case "fill_blank":
                return "✏️";
            case "choose_correct":
                return "🎯";
            case "complete_sentence":
                return "🔗";
            case "correct_sentence":
                return "🔧";
            default:
                return "❓";
        }
    };

    const getQuestionTypeColor = (type: string) => {
        switch (type) {
            case "fill_blank":
                return "bg-blue-500";
            case "choose_correct":
                return "bg-green-500";
            case "complete_sentence":
                return "bg-purple-500";
            case "correct_sentence":
                return "bg-orange-500";
            default:
                return "bg-gray-500";
        }
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
                </div>                {/* Score Summary */}
                <div className="bg-white rounded-3xl shadow-2xl p-8 mb-8">
                    <div className="text-center">
                        <div className="text-8xl mb-4">{getScoreEmoji(results.results.accuracy)}</div>
                        <div className={`text-6xl font-bold mb-4 ${getScoreColor(results.results.accuracy)}`}>
                            {results.results.accuracy}%
                        </div>
                        <h2 className="text-3xl font-bold text-gray-800 mb-2">
                            {getScoreMessage(results.results.accuracy)}
                        </h2>
                        <p className="text-xl text-gray-600 mb-6">
                            You scored {results.results.score} out of {results.results.total_questions} points
                        </p>

                        {/* Score Breakdown */}
                        <div className="grid grid-cols-3 gap-4 mb-8">
                            <div className="bg-blue-50 rounded-xl p-4">
                                <div className="text-2xl font-bold text-blue-600">{results.results.score}</div>
                                <div className="text-blue-800 font-medium">Correct</div>
                            </div>
                            <div className="bg-red-50 rounded-xl p-4">
                                <div className="text-2xl font-bold text-red-600">{results.results.total_questions - results.results.score}</div>
                                <div className="text-red-800 font-medium">Incorrect</div>
                            </div>
                            <div className="bg-purple-50 rounded-xl p-4">
                                <div className="text-2xl font-bold text-purple-600">{results.results.total_questions}</div>
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
                </div>                {/* Detailed Results */}
                <div className="space-y-4">
                    <h3 className="text-2xl font-bold text-white mb-4">Detailed Review</h3>
                    {results.results.answers_history.map((answer, index) => (
                        <div key={index} className="bg-white rounded-2xl shadow-lg p-6">
                            <div className="flex items-start gap-4">
                                {/* Question Type Icon */}
                                <div className={`w-12 h-12 ${getQuestionTypeColor(answer.question.type)} rounded-xl flex items-center justify-center text-white text-xl flex-shrink-0`}>
                                    {getQuestionTypeIcon(answer.question.type)}
                                </div>

                                <div className="flex-1">
                                    {/* Question Header */}
                                    <div className="flex items-center justify-between mb-3">
                                        <h4 className="font-bold text-lg text-gray-800">
                                            Question {index + 1}
                                        </h4>
                                        <div className={`px-4 py-2 rounded-full text-sm font-bold ${answer.is_correct
                                            ? "bg-green-100 text-green-800"
                                            : "bg-red-100 text-red-800"
                                            }`}>
                                            {answer.is_correct ? "✓ Correct" : "✗ Incorrect"}
                                        </div>
                                    </div>

                                    {/* Question */}
                                    <p className="text-gray-700 mb-3 font-medium">{answer.question.prompt}</p>

                                    {/* Answer Details */}
                                    <div className="mb-4">
                                        <p className="text-sm font-semibold text-gray-600 mb-1">Your Answer:</p>
                                        <p className={`font-medium ${answer.is_correct ? "text-green-600" : "text-red-600"}`}>
                                            {answer.user_answer}
                                        </p>
                                    </div>

                                    {/* Feedback */}
                                    <div className="p-4 bg-gray-50 rounded-xl">
                                        <p className="text-sm font-semibold text-gray-600 mb-2">Feedback:</p>
                                        <div className="text-sm text-gray-700 whitespace-pre-line">
                                            {answer.feedback}
                                        </div>
                                    </div>
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
