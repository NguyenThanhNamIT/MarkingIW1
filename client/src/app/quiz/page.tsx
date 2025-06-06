"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { API_BASE_URL } from "@/api/config";

interface Question {
    type: string;
    prompt: string;
    instruction: string;
}

interface QuizState {
    state: string;
    current_question: number;
    total_questions: number;
    total_score: number;
    current_question_data: Question | null;
}

export default function QuizPage() {
    const [quizState, setQuizState] = useState<QuizState | null>(null);
    const [userAnswer, setUserAnswer] = useState("");
    const [timeLeft, setTimeLeft] = useState(30);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [showFeedback, setShowFeedback] = useState(false);
    const [feedback, setFeedback] = useState("");
    const [firstVerb, setFirstVerb] = useState("");
    const [isAwaitingSecondVerb, setIsAwaitingSecondVerb] = useState(false);
    const router = useRouter();

    // Timer countdown
    useEffect(() => {
        if (timeLeft > 0 && !showFeedback && quizState?.state !== "start") {
            const timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000);
            return () => clearTimeout(timer);
        } else if (timeLeft === 0 && !showFeedback) {
            handleSubmitAnswer();
        }
    }, [timeLeft, showFeedback, quizState]);

    // Fetch initial quiz status
    useEffect(() => {
        fetchQuizStatus();
    }, []);

    const fetchQuizStatus = async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/status`, {
                credentials: "include",
            });
            const data = await response.json();
            setQuizState(data);
            setTimeLeft(30);
        } catch (error) {
            console.error("Error fetching quiz status:", error);
        }
    };

    const handleSubmitAnswer = async () => {
        if (isSubmitting) return;

        setIsSubmitting(true); try {
            let answerToSubmit = userAnswer;

            // Handle complete questions that need two verbs
            if (quizState?.current_question_data?.type === "complete" && isAwaitingSecondVerb) {
                answerToSubmit = userAnswer; // This is the second verb
            } else if (quizState?.current_question_data?.type === "complete" && !isAwaitingSecondVerb) {
                // This is the first verb, send it to server and wait for prompt for second verb
                answerToSubmit = userAnswer; // Send first verb to server
                setFirstVerb(userAnswer); // Keep track locally for UI
            }

            const response = await fetch(`${API_BASE_URL}/answer`, {
                method: "POST",
                credentials: "include",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ answer: answerToSubmit }),
            });

            const data = await response.json(); if (data.success) {
                // Check if this is a request for the second verb (complete questions)
                if (data.message && data.message.includes("Enter the second verb")) {
                    // This is the response to the first verb in a complete question
                    setIsAwaitingSecondVerb(true);
                    setUserAnswer("");
                    setTimeLeft(30); // Reset timer for second verb
                    setIsSubmitting(false);
                    return; // Don't show feedback, just wait for second verb
                }

                setFeedback(data.message);
                setShowFeedback(true);
                setQuizState(data);// Auto-advance after showing feedback
                setTimeout(() => {
                    if (data.state === "start") {
                        // Quiz completed, go to results
                        router.push("/results");
                    } else {
                        // Next question - data already contains next question info
                        setShowFeedback(false);
                        setUserAnswer("");
                        setFirstVerb("");
                        setIsAwaitingSecondVerb(false);
                        setTimeLeft(30);
                        // No need to fetch status again, data already has next question
                    }
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
    };

    const getProgressPercentage = () => {
        if (!quizState) return 0;
        return ((quizState.current_question + 1) / quizState.total_questions) * 100;
    };

    const getQuestionTypeColor = (type: string) => {
        switch (type) {
            case "blank": return "bg-blue-500";
            case "choose": return "bg-green-500";
            case "complete": return "bg-purple-500";
            case "correct": return "bg-orange-500";
            default: return "bg-gray-500";
        }
    };

    const getQuestionTypeIcon = (type: string) => {
        switch (type) {
            case "blank": return "✏️";
            case "choose": return "🎯";
            case "complete": return "🔗";
            case "correct": return "🔧";
            default: return "❓";
        }
    };

    if (!quizState || !quizState.current_question_data) {
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
                            {feedback.includes("Correct") ? "🎉" : "😞"}
                        </div>
                        <h2 className="text-3xl font-bold mb-4">
                            {feedback.includes("Correct") ? "Correct!" : "Incorrect"}
                        </h2>
                        <p className="text-gray-600 text-lg mb-6">{feedback}</p>
                        <div className="text-sm text-gray-500">
                            Moving to next question...
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-600 to-purple-600 p-4">
            {/* Header */}
            <div className="max-w-4xl mx-auto mb-6">
                <div className="bg-white rounded-2xl shadow-lg p-4">
                    <div className="flex items-center justify-between mb-4">
                        <div className="flex items-center gap-4">
                            <div className={`w-12 h-12 ${getQuestionTypeColor(quizState.current_question_data.type)} rounded-xl flex items-center justify-center text-white text-xl`}>
                                {getQuestionTypeIcon(quizState.current_question_data.type)}
                            </div>
                            <div>
                                <h1 className="text-xl font-bold">Question {quizState.current_question + 1}</h1>
                                <p className="text-gray-600 capitalize">{quizState.current_question_data.type} Question</p>
                            </div>
                        </div>
                        <div className="text-right">
                            <div className="text-2xl font-bold text-purple-600">{timeLeft}s</div>
                            <div className="text-sm text-gray-600">Time Left</div>
                        </div>
                    </div>

                    {/* Progress Bar */}
                    <div className="w-full bg-gray-200 rounded-full h-3">
                        <div
                            className="bg-gradient-to-r from-purple-500 to-pink-500 h-3 rounded-full transition-all duration-300"
                            style={{ width: `${getProgressPercentage()}%` }}
                        ></div>
                    </div>
                    <div className="text-sm text-gray-600 mt-2">
                        {quizState.current_question + 1} of {quizState.total_questions} questions
                    </div>
                </div>
            </div>

            {/* Question Card */}
            <div className="max-w-4xl mx-auto">
                <div className="bg-white rounded-3xl shadow-2xl p-8">
                    {/* Instructions */}
                    <div className="bg-blue-50 rounded-xl p-4 mb-6">
                        <h3 className="font-semibold text-blue-800 mb-2">Instructions:</h3>
                        <p className="text-blue-700">{quizState.current_question_data.instruction}</p>
                    </div>

                    {/* Question */}
                    <div className="mb-8">
                        <h2 className="text-2xl font-bold text-gray-800 mb-4">
                            {isAwaitingSecondVerb ? `Complete the second verb:` : quizState.current_question_data.prompt}
                        </h2>

                        {isAwaitingSecondVerb && (
                            <div className="bg-green-50 rounded-xl p-4 mb-4">
                                <p className="text-green-800">
                                    First verb entered: <span className="font-bold">{firstVerb}</span>
                                </p>
                            </div>
                        )}
                    </div>

                    {/* Answer Input */}
                    <div className="mb-8">
                        {quizState.current_question_data.type === "choose" ? (
                            <div className="grid grid-cols-1 gap-3">
                                {["Past", "Present", "Future", "None of the above"].map((option, index) => (
                                    <button
                                        key={index}
                                        onClick={() => setUserAnswer((index + 1).toString())}
                                        className={`p-4 rounded-xl border-2 text-left transition-all duration-200 ${userAnswer === (index + 1).toString()
                                            ? "border-purple-500 bg-purple-50 text-gray-800"
                                            : "border-gray-200 hover:border-gray-300 text-gray-800"
                                            }`}
                                    >
                                        <span className="font-bold text-purple-600">{index + 1})</span> {option}
                                    </button>
                                ))}
                            </div>
                        ) : (
                            <input
                                type="text"
                                value={userAnswer}
                                onChange={(e) => setUserAnswer(e.target.value)}
                                onKeyPress={handleKeyPress}
                                className="w-full p-4 text-xl border-2 border-gray-300 rounded-xl focus:border-purple-500 focus:outline-none text-gray-800"
                                placeholder="Type your answer here..."
                                disabled={isSubmitting}
                            />
                        )}
                    </div>

                    {/* Submit Button */}
                    <div className="text-center">
                        <button
                            onClick={handleSubmitAnswer}
                            disabled={isSubmitting || !userAnswer}
                            className="bg-gradient-to-r from-purple-600 to-pink-600 text-white text-xl font-bold py-4 px-12 rounded-2xl hover:from-purple-700 hover:to-pink-700 transform hover:scale-105 transition-all duration-300 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
                        >
                            {isSubmitting ? (
                                <div className="flex items-center gap-3">
                                    <div className="w-6 h-6 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                                    Submitting...
                                </div>
                            ) : (
                                isAwaitingSecondVerb ? "Submit Second Verb" : "Submit Answer"
                            )}
                        </button>
                    </div>
                </div>
            </div>

            {/* Score Display */}
            <div className="max-w-4xl mx-auto mt-6">
                <div className="bg-white/20 backdrop-blur-sm rounded-2xl p-4 text-center">
                    <div className="text-white text-lg">
                        Current Score: <span className="font-bold">{quizState.total_score}</span> / 8
                    </div>
                </div>
            </div>
        </div>
    );
}
