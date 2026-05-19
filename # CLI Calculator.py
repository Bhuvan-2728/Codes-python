# CLI Calculator

def calculate(a, b, op):
    if   op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/':
        if b == 0: raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operator")

def main():
    print("=== Python Calculator ===")
    while True:
        try:
            a  = float(input("Enter first number : "))
            op = input("Operator (+, -, *, /): ").strip()
            b  = float(input("Enter second number: "))
            result = calculate(a, b, op)
            print(f"Result: {a} {op} {b} = {result}\n")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}\n")
        again = input("Calculate again? (y/n): ").lower()
        if again != 'y': break

if __name__ == "__main__": main()