from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


# 🏠 HOME ROUTE
@app.route('/')
def home():
    return render_template('index.html')


# ✨ FORMAT FUNCTION (clean spacing)
def format_reply(text):
    return text.strip().replace("  ", " ")


# 💬 CHAT ROUTE
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        if not data or 'text' not in data:
            return jsonify({"reply": "Please enter a message."})

        text = data['text']
        text_lower = text.lower()

        print("User:", text)

        # 💙 SAD / LOW
        if any(word in text_lower for word in [
            "sad", "alone", "tired", "depressed", "low", "upset", "cry"
        ]):
            reply = (
                "I'm really glad you shared this 💙\n\n"
                "You're not alone… I'm here with you.\n\n"
                "Want to tell me what's been bothering you?"
            )

        # 😠 ANGER / FRUSTRATION
        elif any(word in text_lower for word in [
            "angry", "frustrated", "mad", "annoyed", "irritated"
        ]):
            reply = (
                "That sounds really frustrating 😌\n\n"
                "It's okay to feel this way.\n\n"
                "Do you want to talk about what happened?"
            )

        # 😰 ANXIETY / WORRY
        elif any(word in text_lower for word in [
            "anxious", "worried", "nervous", "scared", "fear"
        ]):
            reply = (
                "I understand… that feeling can be overwhelming 🤝\n\n"
                "You're safe here.\n\n"
                "Want to share what’s worrying you?"
            )

        # 😊 POSITIVE / HAPPY
        elif any(word in text_lower for word in [
            "happy", "good", "amazing", "great", "excited", "love", "enjoy"
        ]):
            reply = (
                "That’s wonderful to hear 😊\n\n"
                "Moments like these really matter.\n\n"
                "Tell me more about it!"
            )

        # ⚖️ MIXED FEELINGS
        elif any(word in text_lower for word in [
            "but", "however", "still", "although"
        ]):
            reply = (
                "It sounds like you're feeling a mix of emotions 💙\n\n"
                "That’s completely okay.\n\n"
                "Want to talk more about it?"
            )

        # 💬 DEFAULT
        else:
            reply = (
                "I'm here to listen 💙\n\n"
                "Take your time… tell me more."
            )

        return jsonify({"reply": reply})
    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"reply": "⚠️ Something went wrong. Please try again."})


# 🚀 RUN APP


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses PORT
    app.run(host="0.0.0.0", port=port)
