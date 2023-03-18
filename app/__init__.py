from flask import Flask

app=Flask(__name__)

from app.routes import gpt3
from app.routes import health
