# quiz.py — Multiple Choice Quiz App

QUESTIONS = [
    {"q": "What is the output of type([])??",
     "options": ["list","array",<class 'list'>,"tuple"], "answer": 2},
    {"q": "Which keyword defines a function?",
     "options": ["func","def","fun","define"], "answer": 1},
    {"q": "Which of these is immutable?",
     "options": ["list","dict","tuple","set"], "answer": 2},
    {"q": "Python index starts at?",
     "options": ["1","0","-1","None"], "answer": 1},
]

def run_quiz():
    score = 0
    print("\n=== Python Quiz ===\n")
    for i, q in enumerate(QUESTIONS, 1):
        print(f"Q{i}: {q['q']}")
        for j, opt in enumerate(q['options']):
            print(f"  {j}. {opt}")
        try:
            ans = int(input("Your answer (0-3): "))
            if ans == q['answer']:
                print("✓ Correct!\n"); score += 1
            else:
                print(f"✗ Wrong. Answer: {q['options'][q['answer']]}\n")
        except: print("Invalid input, skipped.\n")
    pct = score / len(QUESTIONS) * 100
    print(f"Score: {score}/{len(QUESTIONS)} ({pct:.0f}%)")
    grade = "Excellent" if pct >= 80 else "Good" if pct >= 60 else "Keep practicing!"
    print(f"Grade: {grade}")

if __name__ == "__main__": run_quiz()