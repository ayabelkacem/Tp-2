import subprocess

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/ping")
def ping():
    host = request.args.get("host")
    return subprocess.check_output("ping -c 1 " + host, shell=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
