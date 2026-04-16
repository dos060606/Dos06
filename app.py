from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # HTML мен Python-ды байланыстыру үшін керек

# ОСЫ ЖЕРГЕ GOOGLE-ДАН АЛҒАН КІЛТТІ ҚОЙ
genai.configure(api_key="AQ.Ab8RN6LhdK_MT3EfOuxzHsCYZ3lrd76YxOxt_SbF_PE_0J1Y3w")
model = genai.GenerativeModel('gemini-pro')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    try:
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": "Қате орын алды: API кілтті тексеріңіз."}), 500

if __name__ == '__main__':
    app.run(port=5000)
