from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained chatbot model
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        # Generate a response from the chatbot
        response = chatbot(user_message)
        chatbot_reply = response[0]['generated_text']
        return jsonify({'reply': chatbot_reply})
    return jsonify({'reply': 'Sorry, I did not understand your message.'})

if __name__ == "__main__":
    app.run(debug=True)
