import re
import subprocess

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    if not re.fullmatch(r"[A-Za-z0-9.\-]{1,253}", host):
        return "Invalid host", 400
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
