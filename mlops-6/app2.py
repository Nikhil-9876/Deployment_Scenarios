from flask import Flask, request
from waitress import serve

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.host == "api.abcdmihir.com":
        return "Go to abcdmihir.com"
    return "Another API Page here"

if __name__ == "__main__":
    serve(app,host="0.0.0.0",port=5002)