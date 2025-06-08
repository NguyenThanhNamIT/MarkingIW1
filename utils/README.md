# Grammar Validation System for Quiz Game Chatbot

This system provides robust English grammar validation using ANTLR (ANother Tool for Language Recognition) to check sentence correctness in real-time.

## 🚀 Features

- **Real-time Grammar Validation**: Instantly validate English sentences for grammatical correctness
- **Subject-Verb Agreement**: Detects mismatches between subjects and verbs
- **Verb Tense Consistency**: Ensures proper tense usage with time expressions
- **Case-Insensitive Processing**: Handles both lowercase and capitalized words
- **Detailed Error Reporting**: Provides specific feedback on grammar issues
- **Easy Integration**: Simple API for use in chatbots and quiz applications

## 📁 Files Overview

- `TenseQuiz.g4` - ANTLR grammar definition file
- `grammar_validator.py` - Core validation module
- `answer_validator.py` - Quiz-specific validation with scoring
- `run.py` - Main script for testing and generation
- `CompiledFiles/` - Generated ANTLR parser files

## 🛠️ Setup

1. **Install ANTLR** (if not already installed):
   ```powershell
   # Download ANTLR jar file to C:/antlr/
   # Update ANTLR_JAR path in run.py if different
   ```

2. **Install Python Dependencies**:
   ```powershell
   pip install antlr4-python3-runtime
   ```

3. **Generate Parser Files**:
   ```powershell
   cd utils
   python run.py gen
   ```

## 🎯 Usage

### Basic Grammar Validation

```python
from grammar_validator import is_grammar_correct, format_grammar_feedback

# Simple validation
sentence = "She goes to school"
is_correct = is_grammar_correct(sentence)
print(f"Grammar correct: {is_correct}")

# Detailed feedback
feedback = format_grammar_feedback(sentence)
print(feedback)
```

### Quiz Integration

```python
from answer_validator import AnswerValidator

validator = AnswerValidator()

# Validate user answer
user_answer = "I goes to school"  # Incorrect
result = validator.validate_answer(user_answer)

print(f"Valid: {result['is_valid']}")
print(f"Score: {result['score']}")
print(f"Feedback: {result['feedback']}")
```

### Command Line Usage

```powershell
# Test the system
python run.py test

# Validate a specific sentence
python run.py validate "She goes to school"

# Generate ANTLR files
python run.py gen
```

## ✅ Supported Grammar Rules

### Subject-Verb Agreement
- ✅ "She **goes** to school" (3rd person singular + verb+s)
- ❌ "She **go** to school" (incorrect agreement)
- ✅ "They **go** to school" (plural subject + base verb)
- ❌ "They **goes** to school" (incorrect agreement)

### Verb Tenses with Time Expressions
- ✅ "I **went** yesterday" (past tense + past time)
- ❌ "I **will went** yesterday" (mixed tenses)
- ✅ "I **will go** tomorrow" (future tense + future time)
- ❌ "I **went** tomorrow" (wrong tense)

### Sentence Structure
- Subject + Verb + (Object) + (Prepositional Phrase) + (Time Expression)
- Fill-in-the-blank answers (single verbs)

## 🔧 Integration with Your Chatbot

### Flask Server Integration

Add to your `server/app.py`:

```python
import sys
sys.path.append('../utils')
from answer_validator import AnswerValidator

validator = AnswerValidator()

@app.route('/validate_answer', methods=['POST'])
def validate_answer():
    data = request.json
    user_answer = data.get('answer', '')
    
    result = validator.validate_answer(user_answer)
    
    return jsonify({
        'is_valid': result['is_valid'],
        'score': result['score'],
        'feedback': result['feedback'],
        'grammar_correct': result['grammar_correct']
    })
```

### Next.js Client Integration

Add validation API call in your client:

```typescript
// src/api/validation.ts
export async function validateAnswer(answer: string) {
  const response = await fetch('/api/validate_answer', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ answer })
  });
  
  return response.json();
}
```

## 📊 Error Types and Solutions

| Error Type | Example | Solution |
|------------|---------|----------|
| Subject-Verb Disagreement | "She go" | Use "She goes" |
| Wrong Tense | "I will went" | Use "I went" or "I will go" |
| Mixed Time/Tense | "Tomorrow I went" | Use "Yesterday I went" |

## 🧪 Testing

Run comprehensive tests:

```powershell
# Run all tests
python run.py test

# Test specific functionality
python test_grammar.py

# Test answer validator
python answer_validator.py
```

## 📈 Performance Notes

- **Speed**: ~10-50ms per sentence validation
- **Memory**: Minimal footprint with cached parser
- **Accuracy**: High precision for common grammar rules
- **Scalability**: Suitable for real-time applications

## 🔮 Future Enhancements

- [ ] More complex sentence structures
- [ ] Passive voice detection
- [ ] Advanced punctuation rules
- [ ] Multi-sentence validation
- [ ] Grammar suggestions (not just error detection)

## 🚨 Troubleshooting

### Common Issues

1. **"No module named 'CompiledFiles'"**
   ```powershell
   python run.py gen  # Regenerate parser files
   ```

2. **ANTLR jar file not found**
   - Update `ANTLR_JAR` path in `run.py`
   - Ensure ANTLR jar is downloaded

3. **Import errors**
   - Check Python path includes utils directory
   - Verify all dependencies installed

### Debug Mode

Enable verbose logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📞 Support

For issues or questions about the grammar validation system, check the error messages provided by the validation functions - they often contain specific guidance for fixing grammar issues.

---

**Created for IU Senior Project - Quiz Game Chatbot**  
*Enhancing language learning through intelligent grammar validation*
