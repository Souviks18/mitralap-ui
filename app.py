from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    rasa_url = "https://mitralap-bot.onrender.com/webhooks/rest/webhook"

    payload = {"message": user_message}
    response = requests.post(rasa_url, json=payload)

    messages = []
    if response.status_code == 200:
        responses = response.json()
        for r in responses:
            messages.append(r.get("text"))
    return jsonify({"responses": messages})

if __name__ == "__main__":
    app.run(debug=True)
