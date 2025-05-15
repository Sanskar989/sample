def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= num
    return result

def get_numbers():
    while True:
        raw = input("Enter numbers separated by space: ")
        try:
            numbers = list(map(float, raw.strip().split()))
            if len(numbers) < 2:
                print("Please enter at least two numbers.")
                continue
            return numbers
        except ValueError:
            print("Invalid input. Only numeric values are allowed.")

def main():
    print("🔢 Safe N-Input CLI Calculator")
    print("Operations: +  -  *  /")
    print("Type 'q' to quit.\n")

    while True:
        try:
            op = input("Enter operation (+, -, *, / or q): ").strip()
            if op.lower() == 'q':
                print("👋 Exiting calculator. Goodbye!")
                break

            if op not in ['+', '-', '*', '/']:
                print(" Invalid operation. Use only +, -, *, /")
                continue

            numbers = get_numbers()

            if op == '+':
                result = add(numbers)
            elif op == '-':
                result = subtract(numbers)
            elif op == '*':
                result = multiply(numbers)
            elif op == '/':
                result = divide(numbers)

            print(f" Result: {result}\n")

        except ZeroDivisionError as zde:
            print("", zde, "\n")
        except Exception as e:
            print(" Unexpected error:", e, "\n")

if __name__ == "__main__":
    main()