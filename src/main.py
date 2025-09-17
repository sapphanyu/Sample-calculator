def get_numbers_and_operator():
    """
    Prompts the user to enter two numbers and an operator in (num1 x num2) format.
    Handles non-numeric input and incorrect format.
    Returns a tuple of (num1, num2, operator) if successful, otherwise None.
    """
    while True:
        num_string = input("Enter two numbers and one operator in (num1 operator num2) format\noperator choice(+, -, *, /, **): ").strip()
        parts = num_string.split()

        if len(parts) != 3:
            print("Invalid format. Please use (num1 operator num2) format.")
            continue

        num1_str, operator, num2_str = parts

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
            if operator in ['+', '-', '*', '/', '**']:
                return num1, num2, operator
            else:
                print(f"Invalid operator: {operator}. Please choose from +, -, *, /, **.")
        except ValueError:
            print("Invalid number input. Please enter valid numbers.")


def add_numbers(num1, num2):
    """Performs addition of two numbers."""
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")

def subtract_numbers(num1, num2):
    """Performs subtraction of two numbers."""
    result = num1 - num2
    print(f"The result of {num1} - num2 is: {result}")

def multiply_numbers(num1, num2):
    """Performs multiplication of two numbers."""
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")

def divide_numbers(num1, num2):
    """Performs division of two numbers."""
    if num2 == 0:
        print("Cannot divide by zero!")
        return
    else:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")

def power_numbers(num1, num2):
    """Performs exponentiation of two numbers."""
    result = num1 ** num2
    print(f"The result of {num1} ** {num2} is: {result}")


# Main program loop
def main():
    print("Welcome to the Simple CLI Calculator!")
    print("Available commands: quit, or enter 'calculate' to perform a calculation")
    print("Supported operators: +, -, *, /, **")

    while True:
        user_command = input("\nEnter a command (calculate or quit): ").lower().strip()

        if user_command == 'quit':
            print("Exiting calculator. Goodbye!")
            break
        elif user_command == 'calculate':
            calculation_parts = get_numbers_and_operator()
            if calculation_parts:
                num1, num2, operator = calculation_parts
                if operator == '+':
                    add_numbers(num1, num2)
                elif operator == '-':
                    subtract_numbers(num1, num2)
                elif operator == '*':
                    multiply_numbers(num1, num2)
                elif operator == '/':
                    divide_numbers(num1, num2)
                elif operator == '**':
                    power_numbers(num1, num2)
        else:
            print("Invalid command. Please enter 'calculate' or 'quit'.")


if __name__ == "__main__":
    main()