from flask import request
from app import app
from app.services import gpt3

@app.route("/gpt3", methods=["POST"])
def gpt3_endpoint():
    return gpt3.generate_text()