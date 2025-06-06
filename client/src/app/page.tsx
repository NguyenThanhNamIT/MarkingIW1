"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { API_BASE_URL } from "@/api/config";

export default function Home() {
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter(); const startQuiz = async () => {
    setIsLoading(true);
    try {
      // Reset any existing game state first
      await fetch(`${API_BASE_URL}/reset`, {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
        },
      });

      // Start a new quiz
      const response = await fetch(`${API_BASE_URL}/start`, {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        router.push("/quiz");
      } else {
        console.error("Failed to start quiz");
        setIsLoading(false);
      }
    } catch (error) {
      console.error("Error starting quiz:", error);
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-600 via-pink-500 to-indigo-600 flex items-center justify-center p-4">
      <div className="max-w-2xl w-full text-center">
        {/* Logo/Title */}
        <div className="mb-8">
          <h1 className="text-6xl font-bold text-white mb-4 drop-shadow-lg">
            Grammar Quiz
          </h1>
          <p className="text-xl text-white/90 font-medium">
            Master English Grammar with Interactive Exercises
          </p>
        </div>

        {/* Main Card */}
        <div className="bg-white rounded-3xl shadow-2xl p-8 mb-8 transform hover:scale-105 transition-transform duration-300">
          <div className="mb-6">
            <div className="text-6xl mb-4">📚</div>
            <h2 className="text-3xl font-bold text-gray-800 mb-4">
              English Grammar Challenge
            </h2>
            <p className="text-gray-600 text-lg leading-relaxed">
              Test your knowledge of English tenses with 8 interactive questions.
              Fill in blanks, choose correct answers, complete sentences, and fix grammar mistakes!
            </p>
          </div>

          {/* Quiz Features */}
          <div className="grid grid-cols-2 gap-4 mb-8">
            <div className="bg-blue-50 rounded-xl p-4">
              <div className="text-2xl mb-2">⏱️</div>
              <div className="font-semibold text-blue-800">Timed Questions</div>
              <div className="text-sm text-blue-600">30 seconds per question</div>
            </div>
            <div className="bg-green-50 rounded-xl p-4">
              <div className="text-2xl mb-2">🎯</div>
              <div className="font-semibold text-green-800">8 Questions</div>
              <div className="text-sm text-green-600">Mixed question types</div>
            </div>
            <div className="bg-yellow-50 rounded-xl p-4">
              <div className="text-2xl mb-2">🏆</div>
              <div className="font-semibold text-yellow-800">Instant Feedback</div>
              <div className="text-sm text-yellow-600">Learn as you play</div>
            </div>
            <div className="bg-purple-50 rounded-xl p-4">
              <div className="text-2xl mb-2">📊</div>
              <div className="font-semibold text-purple-800">Detailed Results</div>
              <div className="text-sm text-purple-600">Track your progress</div>
            </div>
          </div>

          {/* Start Button */}
          <button
            onClick={startQuiz}
            disabled={isLoading}
            className="bg-gradient-to-r from-purple-600 to-pink-600 text-white text-xl font-bold py-4 px-12 rounded-2xl hover:from-purple-700 hover:to-pink-700 transform hover:scale-105 transition-all duration-300 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
          >
            {isLoading ? (
              <div className="flex items-center gap-3">
                <div className="w-6 h-6 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                Starting Quiz...
              </div>
            ) : (
              "Start Quiz 🚀"
            )}
          </button>
        </div>

        {/* Footer */}
        <div className="text-white/70 text-sm">
          Ready to challenge your English grammar skills? Let's begin!
        </div>
      </div>
    </div>
  );
}
