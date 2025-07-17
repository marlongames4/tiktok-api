from flask import Flask, jsonify
import requests
import re
import os
import json

app = Flask(__name__)

def get_followers(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    try:
        data_text = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.+?)</script>', response.text)
        if not data_text:
            return -1
        json_data = json.loads(data_text.group(1))
        user_info = json_data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
        return user_info['stats']['followerCount']
    except Exception as e:
        print("Erro:", e)
        return -1

@app.route("/api/seguidores", methods=["GET"])
def seguidores():
    username = "minefurry"  # ou seu @ real
    count = get_followers(username)
    return jsonify({"seguidores": count})

# >>> ESSA PARTE É ESSENCIAL PRO RENDER FUNCIONAR
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
