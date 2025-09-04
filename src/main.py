# simple_calculator_week1.py

def main():
    """
    Main function for the Simple Calculator Week 1.
    Handles the main loop, 'quit' command, and simple addition.
    """
    print("Welcome to Simple Calculator!") # Display a welcome message

    while True:
        # Prompt the user for a command and convert it to lowercase
        # for case-insensitive command recognition (e.g., 'Quit' works like 'quit').
        command = input("\nChoose an option: add, quit\n> ").lower()

        if command == 'quit':
            print("Goodbye!")
            # Exit the program loop as requested by the 'quit' command.
            break
        elif command == 'add':
            # This block handles the addition operation.
            # It prompts the user for two numbers.
            num1_str = input("Enter the first number: ")
            num2_str = input("Enter the second number: ")

            # Convert the input strings to floating-point numbers.
            # NOTE for Debugger (Four):
            # As per Week 1 plan, the Coder's task is to convert inputs to numbers.
            # The Debugger (Four) is responsible for testing edge cases like non-numeric input.
            # If a user enters text instead of numbers (e.g., "hello"),
            # this conversion will raise a ValueError, causing the program to crash.
            # This crash is an expected "Whoops!" moment for the Debugger to identify
            # and report for future improvements (e.g., adding try-except blocks in later sprints).
            num1 = float(num1_str)
            num2 = float(num2_str)

            # Perform the addition operation.
            result = num1 + num2

            # Display the result to the user clearly.
            print(f"Result: {num1} + {num2} = {result}")
        else:
            # Inform the user if an invalid command is entered.
            print("Invalid command. Please try again.")

# This ensures that the 'main()' function is called only when the script is executed directly.
if __name__ == "__main__":
    main()
