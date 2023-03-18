from flask import request
from app import app
from app.services import health

@app.route("/health", methods=["GET"])
def health_endpoint():
    return health.health_check()