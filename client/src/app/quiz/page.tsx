"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { API_BASE_URL } from "@/api/config";

interface Question {
    id: string;
    type: string;
    prompt: string;
}

interface QuizState {
    success: boolean;
    game_active: boolean;
    game_id?: string;
    score: number;
    total_questions: number;
    max_questions: number;
    current_question: Question | null;
}

export default function QuizPage() {
    const [quizState, setQuizState] = useState<QuizState | null>(null);
    const [userAnswer, setUserAnswer] = useState("");
    const [timeLeft, setTimeLeft] = useState(30);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [showFeedback, setShowFeedback] = useState(false);
    const [feedback, setFeedback] = useState("");
    const router = useRouter();    // Timer countdown
    useEffect(() => {
        if (timeLeft > 0 && !showFeedback && quizState?.game_active) {
            const timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000);
            return () => clearTimeout(timer);
        } else if (timeLeft === 0 && !showFeedback) {
            handleSubmitAnswer();
        }
    }, [timeLeft, showFeedback, quizState]);

    // Fetch initial quiz status
    useEffect(() => {
        fetchQuizStatus();
    }, []); const fetchQuizStatus = async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/status`, {
                credentials: "include",
            });
            const data = await response.json();

            if (data.success && data.game_active && data.current_question) {
                setQuizState(data);
                setTimeLeft(30);
            } else {
                // No active game, redirect to home
                router.push("/");
            }
        } catch (error) {
            console.error("Error fetching quiz status:", error);
            router.push("/");
        }
    };

    const handleSubmitAnswer = async () => {
        if (isSubmitting) return;

        setIsSubmitting(true);

        try {
            const response = await fetch(`${API_BASE_URL}/answer`, {
                method: "POST",
                credentials: "include",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ answer: userAnswer }),
            });

            const data = await response.json(); if (data.success) {
                setFeedback(data.feedback || "Answer submitted");
                setShowFeedback(true);

                // Auto-advance after showing feedback
                setTimeout(() => {
                    if (data.game_complete) {
                        // Quiz completed, go to results
                        router.push("/results");
                    } else if (data.next_question) {
                        // Update quiz state with next question
                        setQuizState(prev => prev ? {
                            ...prev,
                            score: data.score,
                            total_questions: data.total_questions,
                            max_questions: data.max_questions || 10,
                            current_question: data.next_question
                        } : null);
                        setShowFeedback(false);
                        setUserAnswer("");
                        setTimeLeft(30);
                    } else {
                        // Fallback: fetch status to get next question
                        setShowFeedback(false);
                        setUserAnswer("");
                        setTimeLeft(30);
                        fetchQuizStatus();
                    }
                }, 2000);
            } else {
                setFeedback(data.error || "An error occurred");
                setShowFeedback(true);
                setTimeout(() => {
                    setShowFeedback(false);
                }, 2000);
            }
        } catch (error) {
            console.error("Error submitting answer:", error);
        }

        setIsSubmitting(false);
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === "Enter" && !isSubmitting) {
            handleSubmitAnswer();
        }
    }; const getQuestionTypeColor = (type: string) => {
        switch (type) {
            case "blank": return "bg-blue-500";
            case "correct": return "bg-orange-500";
            default: return "bg-gray-500";
        }
    };

    const getQuestionTypeIcon = (type: string) => {
        switch (type) {
            case "blank": return "✏️";
            case "correct": return "🔧";
            default: return "❓";
        }
    }; if (!quizState || !quizState.current_question) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-blue-600 to-purple-600 flex items-center justify-center">
                <div className="text-white text-xl">Loading quiz...</div>
            </div>
        );
    }

    if (showFeedback) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-blue-600 to-purple-600 flex items-center justify-center p-4">
                <div className="max-w-2xl w-full text-center">
                    <div className="bg-white rounded-3xl shadow-2xl p-8">
                        <div className="text-6xl mb-4">
                            {feedback.includes("Correct") || feedback.includes("valid") ? "🎉" : "😞"}
                        </div>
                        <h2 className="text-3xl font-bold mb-4">
                            {feedback.includes("Correct") || feedback.includes("valid") ? "Correct!" : "Incorrect"}
                        </h2>
                        <p className="text-gray-600 text-lg mb-6">{feedback}</p>
                        <div className="text-sm text-gray-500">
                            Moving to next question...
                        </div>
                    </div>
                </div>
            </div>
        );
    } return (
        <div className="min-h-screen bg-gradient-to-br from-blue-600 to-purple-600 p-4">
            {/* Header with Progress */}
            <div className="max-w-4xl mx-auto mb-6">
                <div className="bg-white rounded-2xl shadow-lg p-6">
                    {/* Question Progress Bar */}
                    <div className="mb-4">
                        <div className="flex justify-between items-center mb-2">
                            <span className="text-sm font-semibold text-gray-700">Progress</span>
                            <span className="text-sm font-semibold text-gray-700">
                                {quizState.total_questions + 1} / {quizState.max_questions}
                            </span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-3">
                            <div
                                className="bg-gradient-to-r from-green-500 to-blue-500 h-3 rounded-full transition-all duration-500 ease-out"
                                style={{
                                    width: `${((quizState.total_questions + 1) / quizState.max_questions) * 100}%`
                                }}
                            ></div>
                        </div>
                    </div>

                    {/* Timer Progress Bar */}
                    <div className="mb-4">
                        <div className="flex justify-between items-center mb-2">
                            <span className="text-sm font-semibold text-gray-700">Time Remaining</span>
                            <span className="text-sm font-semibold text-purple-600">{timeLeft}s</span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                            <div
                                className={`h-2 rounded-full transition-all duration-1000 ease-linear ${timeLeft > 15 ? 'bg-green-500' :
                                        timeLeft > 5 ? 'bg-yellow-500' : 'bg-red-500'
                                    }`}
                                style={{
                                    width: `${(timeLeft / 30) * 100}%`
                                }}
                            ></div>
                        </div>
                    </div>

                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-4">
                            <div className={`w-12 h-12 ${getQuestionTypeColor(quizState.current_question.type)} rounded-xl flex items-center justify-center text-white text-xl`}>
                                {getQuestionTypeIcon(quizState.current_question.type)}
                            </div>
                            <div>
                                <h1 className="text-xl font-bold">Question {quizState.total_questions + 1}</h1>
                                <p className="text-gray-600 capitalize">{quizState.current_question.type} Question</p>
                            </div>
                        </div>
                        <div className="text-right">
                            <div className="text-2xl font-bold text-purple-600">{quizState.score}</div>
                            <div className="text-sm text-gray-600">Score</div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Question Card */}
            <div className="max-w-4xl mx-auto">
                <div className="bg-white rounded-3xl shadow-2xl p-8">                    {/* Instructions */}
                    <div className="bg-blue-50 rounded-xl p-4 mb-6">
                        <h3 className="font-semibold text-blue-800 mb-2">Instructions:</h3>
                        <p className="text-blue-700">
                            {quizState.current_question.type === "blank"
                                ? "Fill in the blank with the correct VERB form."
                                : "Correct the grammar in the sentence provided and REWRITE THE WHOLE SENTENCE."
                            }
                        </p>
                    </div>

                    {/* Question */}
                    <div className="mb-8">
                        <h2 className="text-2xl font-bold text-gray-800 mb-4">
                            {quizState.current_question.prompt}
                        </h2>
                    </div>

                    {/* Answer Input - Only text input since we only have blank and correct types */}
                    <div className="mb-8">
                        <input
                            type="text"
                            value={userAnswer}
                            onChange={(e) => setUserAnswer(e.target.value)}
                            onKeyPress={handleKeyPress}
                            className="w-full p-4 text-xl border-2 border-gray-300 rounded-xl focus:border-purple-500 focus:outline-none text-gray-800"
                            placeholder="Type your answer here..."
                            disabled={isSubmitting}
                        />
                    </div>

                    {/* Submit Button */}
                    <div className="text-center">
                        <button
                            onClick={handleSubmitAnswer}
                            disabled={isSubmitting || !userAnswer.trim()}
                            className="bg-gradient-to-r from-purple-600 to-pink-600 text-white text-xl font-bold py-4 px-12 rounded-2xl hover:from-purple-700 hover:to-pink-700 transform hover:scale-105 transition-all duration-300 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
                        >
                            {isSubmitting ? (
                                <div className="flex items-center gap-3">
                                    <div className="w-6 h-6 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                                    Submitting...
                                </div>
                            ) : (
                                "Submit Answer"
                            )}
                        </button>
                    </div>
                </div>
            </div>            {/* Score Display */}
            <div className="max-w-4xl mx-auto mt-6">
                <div className="bg-white/20 backdrop-blur-sm rounded-2xl p-4 text-center">
                    <div className="text-white text-lg">
                        Current Score: <span className="font-bold">{quizState.score}</span> / {quizState.total_questions}
                        <span className="text-sm opacity-75 ml-2">
                            ({quizState.total_questions > 0 ? Math.round((quizState.score / quizState.total_questions) * 100) : 0}%)
                        </span>
                    </div>
                    <div className="text-white/70 text-sm mt-1">
                        Questions Remaining: {quizState.max_questions - (quizState.total_questions + 1)}
                    </div>
                </div>
            </div>
        </div>
    );
}
