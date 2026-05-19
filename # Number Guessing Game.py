# Number Guessing Game
import random

LEVELS = {'easy': (1, 50, 10), 'hard': (1, 200, 7)}

def play(level):
    lo, hi, max_tries = LEVELS[level]
    secret = random.randint(lo, hi)
    print(f"\nGuess a number between {lo} and {hi}. You have {max_tries} tries.")
    for attempt in range(1, max_tries + 1):
        try:
            guess = int(input(f"Attempt {attempt}: "))
        except ValueError:
            print("Please enter a number."); continue
        if   guess < secret: print("Too low ↑")
        elif guess > secret: print("Too high ↓")
        else:
            print(f"🎉 Correct! You got it in {attempt} attempt(s).")
            return attempt
    print(f"Game over! The number was {secret}.")
    return None

def main():
    print("=== Guessing Game ===")
    level = input("Choose level (easy/hard): ").strip().lower()
    if level not in LEVELS: level = 'easy'
    play(level)

if __name__ == "__main__": main()