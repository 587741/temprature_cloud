from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

latest_temperature = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/temperature", methods=["POST"])
def receive_temperature():
    global latest_temperature

    data = request.get_json()

    latest_temperature = data["temperature"]

    return {"status": "ok"}


@app.route("/api/temperature", methods=["GET"])
def get_temperature():
    return jsonify({
        "temperature": latest_temperature
    })