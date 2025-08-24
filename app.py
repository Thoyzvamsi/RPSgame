from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    user_choice = request.json.get("choice")
    options = ["Rock", "Paper", "Scissors"]
    computer = random.choice(options)

    if user_choice == computer:
        result = "Draw"
    elif (user_choice == "Rock" and computer == "Scissors") or \
         (user_choice == "Paper" and computer == "Rock") or \
         (user_choice == "Scissors" and computer == "Paper"):
        result = "Win"
    else:
        result = "Lose"

    return jsonify({"user": user_choice, "computer": computer, "result": result})

if __name__ == "__main__":
    app.run(debug=True)

    