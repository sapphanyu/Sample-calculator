#app.py

from flask import Flask, request, jsonify,render_template
import json
import os
import main  # import ฟังก์ชันคำนวณจาก main.py

app = Flask(__name__)

# กำหนดเส้นทางไฟล์ประวัติ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")

# อ่านประวัติ
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# บันทึกประวัติ
def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=2)

@app.route("/CalculateTest", methods=["POST"])
def calculate():
    data = request.get_json()
    num1 = float(data.get("num1"))
    num2 = float(data.get("num2"))
    operator = data.get("operator")

    if operator not in ["+", "-", "*", "/", "**"]:
        return jsonify({"error": "Invalid operator"}), 400

    try:
        if operator == "+":
            result = main.add_numbers(num1, num2)
        elif operator == "-":
            result = main.subtract_numbers(num1, num2)
        elif operator == "*":
            result = main.multiply_numbers(num1, num2)
        elif operator == "/":
            result = main.divide_numbers(num1, num2)
            if result is None:
                return jsonify({"error": "Division by zero"}), 400
        elif operator == "**":
            result = main.power_numbers(num1, num2)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # บันทึกลง history
    history = load_history()
    record = {"num1": num1, "num2": num2, "operator": operator, "result": result}
    history.append(record)
    save_history(history)

    return jsonify(record)

@app.route("/historyTest", methods=["GET"])
def get_history():
    history = load_history()
    return jsonify(history)

@app.route("/historyTest", methods=["DELETE"])
def clear_history():
    save_history([])
    return jsonify({"message": "History cleared."})

#ต้องเขียนโค้ดคำนวณใหม่




# หน้าเว็บ
@app.route("/")
def home_page():
    return render_template("Calculate.html")

@app.route("/h")
def history_page():
    history = load_history()
    return render_template("History.html", history=history)

@app.route("/c", methods=["GET", "POST"])
def calculator_page():
    result = None
    error = None  # เพิ่มตัวแปรเก็บ error
    if request.method == "POST":
        calculation_input = request.form.get("numstring")
        calculation_parts = main.get_numbers_and_operator_butnoprint(calculation_input)

        if isinstance(calculation_parts, str):  # เป็นข้อความ error
            error = calculation_parts
        else:
            num1, num2, operator = calculation_parts
            if operator == '+':
                result = main.add_numbers(num1, num2)
            elif operator == '-':
                result = main.subtract_numbers(num1, num2)
            elif operator == '*':
                result = main.multiply_numbers(num1, num2)
            elif operator == '/':
                result = main.divide_numbers(num1, num2)
                if result is None:
                    error = "Cannot divide by zero!"
            elif operator == '**':
                result = main.power_numbers(num1, num2)

            # บันทึก history ถ้า result ถูกต้อง
            if result is not None and error is None:
                history = load_history()
                record = {"num1": num1, "num2": num2, "operator": operator, "result": result}
                history.append(record)
                save_history(history)

    return render_template("Calculate.html", result=result, error=error)

#if __name__ == "__main__":
    #app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


