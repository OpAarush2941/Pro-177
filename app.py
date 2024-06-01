from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs":5,
        "category":"Sports",
        "word":"Chess"
    },
    {
        "inputs":6,
        "category":"European Country Name",
        "word":"France"
    },
    {
        "inputs":5,
        "category":"Asian Country Name",
        "word":"India"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post-answers", methods=["POST"])
def get_template():
    return jsonify({
        "status": "success",
        "word":random.choice(templates)
    })