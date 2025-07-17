from flask import Flask, jsonify
import requests
import re

app = Flask(__name__)

def get_followers(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    match = re.search(r'"fans":(\d+)', r.text)
    return int(match.group(1)) if match else -1

@app.route("/api/seguidores")
def seguidores():
    username = "minefurry"
    count = get_followers(username)
    return jsonify({"seguidores": count})

if __name__ == "__main__":
    app.run()
