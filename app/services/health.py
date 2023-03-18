import json
import logging
import requests
from flask import request
# from configparser import ConfigParser
#from app import app

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logger.addHandler(handler)
# config = ConfigParser()
# config.read('config/keys_config.cfg')
# API_KEY = config.get('gpt3', 'api_key')


#@app.route('/health')
def health_check():
    return 'Service is up and running', 200

if __name__ == "__main__":
    print("")