def get_numbers():
    """
    ใช้รับค่าพารามิเตอร์ 2 ตัว ตรวจสอบว่าเป็นตัวเลข และคืนค่ากลับไปเป็นตัวเลข 2 ตัว
    """
    while True:
        try:
            num1_str = input("Enter the first number: ")
            num1 = float(num1_str)
            break
        except ValueError:
            print(f"Invalid input: '{num1_str}' is not a valid number. Please try again.")

    while True:
        try:
            num2_str = input("Enter the second number: ")
            num2 = float(num2_str)
            break
        except ValueError:
            print(f"Invalid input: '{num2_str}' is not a valid number. Please try again.")

    return num1, num2

def add_numbers():
    """ฟังก์ชันการบวก"""
    numbers = get_numbers()
    if numbers:
        num1, num2 = numbers
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")

def subtract_numbers():
    """ฟังก์ชันการลบ"""
    numbers = get_numbers()
    if numbers:
        num1, num2 = numbers
        result = num1 - num2
        print(f"The difference between {num1} and {num2} is: {result}")

# โปรแกรมหลัก
def main():
    print("Welcome to the Simple CLI Calculator!")
    print("Available commands: add, subtract, quit")

  """ทำงานเมื่อเป็นจริงเสมอ"""
    while True:
        command = input("\nEnter a command: ").lower().strip() # .strip() removes leading/trailing whitespace

        if command == 'quit':
            print("Exiting calculator. Goodbye!")
            break
          # หยุดการทำงาน
        elif command == 'add':
            add_numbers()
        elif command == 'subtract':
            subtract_numbers()
        else:
            print("Invalid command. Please choose from 'add', 'subtract', or 'quit'.")

if __name__ == "__main__":
    main()

