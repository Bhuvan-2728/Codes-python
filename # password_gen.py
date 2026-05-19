# password_gen.py — Secure Password Generator
import random, string

def generate_password(length=12, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols: chars += "!@#$%^&*()"
    # Guarantee at least one of each category
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
    ]
    if use_symbols: password.append(random.choice("!@#$%^&*()"))
    password += [random.choice(chars) for _ in range(length - len(password))]
    random.shuffle(password)
    return ''.join(password)

def main():
    print("=== Password Generator ===")
    try:
        n = int(input("How many passwords? "))
        length = int(input("Password length (min 8): "))
        length = max(8, length)
        symbols = input("Include symbols? (y/n): ").lower() == 'y'
        print()
        for i in range(n):
            print(f"  {i+1}. {generate_password(length, symbols)}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__": main()