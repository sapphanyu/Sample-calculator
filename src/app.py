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

@app.route("/calculate", methods=["POST"])
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

@app.route("/history", methods=["GET"])
def get_history():
    history = load_history()
    return jsonify(history)

@app.route("/history", methods=["DELETE"])
def clear_history():
    save_history([])
    return jsonify({"message": "History cleared."})

if __name__ == "__main__":
    app.run(debug=True)
