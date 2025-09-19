import json # For handling JSON file operations
import os # For checking file existence

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # path ของ main.py
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")  # เซฟใน src เดียวกัน

#HISTORY_FILE = "history.json" # File to store calculation history   

def load_history(): #โหลดประวัติการคำนวณจากไฟล์ JSON
    """Loads calculation history from a JSON file."""
    if os.path.exists(HISTORY_FILE): #ถ้าไฟล์มีอยู่
        with open(HISTORY_FILE, 'r') as file: #เปิดไฟล์ในโหมดอ่าน
            try:       #พยายามโหลดข้อมูลจากไฟล์
                return json.load(file)
            except json.JSONDecodeError: #ถ้าไฟล์ว่างหรือข้อมูลไม่ถูกต้อง
                return []
    return [] #ถ้าไฟล์ไม่มีอยู่ ให้คืนค่าเป็นลิสต์ว่าง

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

def get_numbers_and_operator_butnoprint():
    while True:
        num_string = input().strip()
        parts = num_string.split()

        if len(parts) != 3:
            return "Invalid format. Please use (num1 operator num2) format."

        num1_str, operator, num2_str = parts

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
            if operator in ['+', '-', '*', '/', '**']:
                return num1, num2, operator
            else:
                return f"Invalid operator: {operator}. Please choose from +, -, *, /, **."
        except ValueError:
            return "Invalid number input. Please enter valid numbers."


def add_numbers(num1, num2):
    """Performs addition of two numbers."""
    result = num1 + num2
    return result

def subtract_numbers(num1, num2):
    """Performs subtraction of two numbers."""
    result = num1 - num2
    return result

def multiply_numbers(num1, num2):
    """Performs multiplication of two numbers."""
    result = num1 * num2
    return result

def divide_numbers(num1, num2):
    """Performs division of two numbers."""
    if num2 == 0:
        print("Cannot divide by zero!")
        return
    else:
        result = num1 / num2
        return result

def power_numbers(num1, num2):
    """Performs exponentiation of two numbers."""
    result = num1 ** num2
    return result


history = [] #ลิสต์เก็บประวัติการคำนวณ
history = load_history() #โหลดประวัติการคำนวณจากไฟล์ JSON

# Main program loop
def main():
    print("Welcome to the Simple CLI Calculator!")
    print("Available commands: calculate , quit , history , clear history")
    print("Supported operators: +, -, *, /, **")

    while True: # เริ่มลูปหลักของโปรแกรม
        user_command = input("\nEnter a command (calculate , quit , history , clear history): ").lower().strip()

        if user_command == 'quit':# ออกจากโปรแกรม
            print("Exiting calculator. Goodbye!")
            break
        elif user_command == 'calculate': # เริ่มการคำนวณ
            calculation_parts = get_numbers_and_operator()
            if calculation_parts:
                num1, num2, operator = calculation_parts
                if operator == '+':
                    result = add_numbers(num1, num2)
                elif operator == '-':
                    result = subtract_numbers(num1, num2)
                elif operator == '*':
                    result = multiply_numbers(num1, num2)
                elif operator == '/':
                    result = divide_numbers(num1, num2)
                    if result is None:
                        continue  # ข้ามไปเริ่มรอบใหม่           
                elif operator == '**':
                    result = power_numbers(num1, num2)
            if result is not None:
                print(f"The result of {num1} {operator} {num2} is: {result}")


            # บันทึกประวัติการคำนวณ
            record = {"num1": num1,"num2": num2,"operator": operator,"result": result} #สร้างเรคคอร์ดการคำนวณ
            
            history.append(record)
            with open(HISTORY_FILE, 'w') as file: #เปิดไฟล์ในโหมดเขียน
                json.dump(history, file, indent=2) #บันทึกประวัติการคำนวณลงในไฟล์ JSON

        elif user_command == 'history': # แสดงประวัติการคำนวณ
            if not history:
                print("No calculations yet.")
            else:
                print("Calculation history:")
                for i, entry in enumerate(history, start=1):
                    print(f"{i}. {entry['num1']} {entry['operator']} {entry['num2']} = {entry['result']}")

        elif user_command == 'clear history': # ล้างประวัติการคำนวณ
            history.clear()
            print("Calculation history cleared.")
            if os.path.exists(HISTORY_FILE):
                os.remove(HISTORY_FILE)
                print("History file deleted.")

            

        else:
            print("Invalid command. Please enter 'calculate', 'history', 'clear history', or 'quit'.")


if __name__ == "__main__":
    main()