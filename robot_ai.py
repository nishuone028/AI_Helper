from flask import Flask, request, jsonify
import requests
import json
from gevent import pywsgi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    url = "https://api.baichuan-ai.com/v1/chat/completions"
    api_key = "sk-3849478cf16e019d3cf7618db0f116e4"
    data = {
        "model": "Baichuan-NPC-Turbo",
        "character_profile": {
            "character_id": 30354
        },
        "messages": [
            {
                "role": "user",
                "content": request.json.get("message")
            }
        ],
        "temperature": 0.8,
        "top_p": 0.98,
        "max_tokens": 512
    }
    json_data = json.dumps(data)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }
    response = requests.post(url, data=json_data, headers=headers, timeout=60)
    if response.status_code == 200:
        response_data = response.json()
        # 假设返回的JSON数据中有一个'choices'字段，包含机器人的回复
        message = response_data['choices'][0]['message']['content']
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": response.text}), 500

if __name__ == "__main__":
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    server.serve_forever()
