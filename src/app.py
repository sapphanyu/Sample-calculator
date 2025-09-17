from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

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
    num1 = data.get("num1")
    num2 = data.get("num2")
    operator = data.get("operator")

    if operator not in ["+", "-", "*", "/", "**"]:
        return jsonify({"error": "Invalid operator"}), 400

    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return jsonify({"error": "Division by zero"}), 400
            result = num1 / num2
        elif operator == "**":
            result = num1 ** num2
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
