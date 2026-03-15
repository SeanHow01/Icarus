"""
Jarvis Voice Backend — Sits between your browser and Claude API.

This keeps your API key safe on the server side (never exposed to the browser).

Usage:
  1. pip install flask anthropic python-dotenv flask-cors
  2. Copy ../.env.example to .env and add your API key
  3. python server.py
  4. Open jarvis.html in your browser
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Anthropic()

# Conversation memory (resets on server restart)
conversation_history = []


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    conversation_history.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=(
            "You are Jarvis, a witty and helpful AI assistant inspired by "
            "the AI from Iron Man. Keep responses concise — under 3 sentences "
            "when possible, since your responses will be spoken aloud. "
            "Be warm, slightly formal, and occasionally dry-humoured."
        ),
        messages=conversation_history,
    )

    reply = response.content[0].text
    conversation_history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})


@app.route("/reset", methods=["POST"])
def reset():
    conversation_history.clear()
    return jsonify({"status": "Conversation cleared, sir."})


if __name__ == "__main__":
    print("Jarvis voice backend running on http://localhost:5000")
    app.run(port=5000, debug=True)
