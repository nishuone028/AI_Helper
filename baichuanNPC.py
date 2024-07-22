# sk-3849478cf16e019d3cf7618db0f116e4

import requests
import json


def do_request():
    url = "https://api.baichuan-ai.com/v1/chat/completions"
    api_key = ""

    data = {
        "model": "Baichuan-NPC-Turbo",
        "character_profile": {
            "character_id": 10020
        },
        "messages": [
            {
                "role": "user",
                "content": "你好，你是谁"
            },
            {
                "role": "assistant",
                "content": "你好，我是小小，是你的朋友啊"
            },
            {
                "role": "user",
                "content": "你几岁了"
            }
        ],
        "temperature": 0.8,
        "top_p": 0.98,
        "max_tokens": 512,
        "stream": True
    }

    json_data = json.dumps(data)

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    response = requests.post(url, data=json_data, headers=headers, timeout=60)

    if response.status_code == 200:
        print("请求成功！")
        print("响应body:", response.text)
        print("请求成功，X-BC-Request-Id:", response.headers.get("X-BC-Request-Id"))
    else:
        print("请求失败，状态码:", response.status_code)
        print("请求失败，body:", response.text)
        print("请求失败，X-BC-Request-Id:", response.headers.get("X-BC-Request-Id"))


if __name__ == "__main__":
    do_request()







