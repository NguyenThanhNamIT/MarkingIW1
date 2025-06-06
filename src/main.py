from chatbot import QuizChatbot

def main():
    chatbot = QuizChatbot()
    print(chatbot.process_input(""))  # Start the conversation
    while True:
        user_input = input().strip()
        response = chatbot.process_input(user_input)
        print(response)
        if "Kết thúc trò chơi!" in response:  # Updated to match chatbot.py
            print("Would you like to play again? (Type 'yes' or 'exit')")
            choice = input().strip().lower()
            if choice == "exit":
                print("Exiting program.")
                break
            elif choice == "yes":
                print(chatbot.process_input("start game"))

if __name__ == "__main__":
    main()