<<<<<<< HEAD
# Quiz Chatbot (Grammar Exercise)
## Setup
1. Install Python 3.13.2, ensure PATH includes Scripts.
2. Run: `python src\main.py`.

## Usage
- Nhập start game để bắt đầu trò chơi.
- Chọn 1 hoặc 2 để chọn câu hỏi phù hợp
- Nếu đúng thì sẽ qua câu tiếp theo

(Hiện tại chỉ đang có 2 câu hỏi và 3 thì cơ bản, đang phát triển thêm)
=======
# IELTS Writing Task 1 Marking Chatbot
## Setup
1. Install Python 3.13.2, ensure PATH includes Scripts.
2. Store `antlr-4.9.2-complete.jar` in `C:\Tools\ANTLR`.
3. Install runtime: `python -m pip install antlr4-python3-runtime==4.9.2`.
4. Generate parser: `java -jar C:\Tools\ANTLR\antlr-4.9.2-complete.jar -Dlanguage=Python3 src\IELTSWriting.g4`.
5. Run: `python src\main.py`.
## Usage
- Enter graph description and writing when prompted.
- Output: Band scores and suggestions.
>>>>>>> origin/main
