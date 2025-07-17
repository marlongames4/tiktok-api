from flask import Flask, jsonify
import requests
import re
import os

app = Flask(__name__)

def get_followers(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    match = re.search(r'"fans":(\d+)', r.text)
    return int(match.group(1)) if match else -1

@app.route("/api/seguidores", methods=["GET"])
def seguidores():
    username = "minefurry"  # ou seu @ real
    count = get_followers(username)
    return jsonify({"seguidores": count})

# >>> ESSA PARTE É ESSENCIAL PRO RENDER FUNCIONAR
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
