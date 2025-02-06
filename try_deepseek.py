import requests
import os

# 设置API密钥和URL
api_key = os.environ.get("HF_TOKEN")
print(api_key)
base_url = "https://api.deepseek.com/v1"

# 定义请求头
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 定义请求数据
chat_payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "请三句话解释一下量子力学的基本原理。"}
    ]
}

reasoner_payload = {
    "model": "deepseek-reasoner",
    "input": "请三句话解释一下量子力学的基本原理。"
}

# 发送请求到deepseek-chat模型
chat_response = requests.post(f"{base_url}/chat/completions", headers=headers, json=chat_payload)
if chat_response.status_code == 200:
    print("deepseek-chat模型响应：", chat_response.json())
else:
    print("deepseek-chat模型请求失败：", chat_response.status_code, chat_response.text)

# 发送请求到deepseek-reasoner模型
reasoner_response = requests.post(f"{base_url}/reasoner/completions", headers=headers, json=reasoner_payload)
if reasoner_response.status_code == 200:
    print("deepseek-reasoner模型响应：", reasoner_response.json())
else:
    print("deepseek-reasoner模型请求失败：", reasoner_response.status_code, reasoner_response.text)