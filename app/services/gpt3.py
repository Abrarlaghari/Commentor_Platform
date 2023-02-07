import json
import logging
import requests
from flask import request
from configparser import ConfigParser
#from app import app

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logger.addHandler(handler)
config = ConfigParser()
config.read('config/keys_config.cfg')
API_KEY = config.get('gpt3', 'api_key')


#@app.route("/gpt3", methods=["POST"])
def generate_text():
    """
    Endpoint that generates text based on the specified emotion.
    """
    try:
        # Extract the emotion from the request
        emotion = request.json['emotion']
        prompt = request.json['prompt']

        # Define the prompt based on the emotion
        # prompt = ""
        if emotion == "funny":
            prompt = "Please make a funny comment on this statement: "+ prompt
        elif emotion == "angry":
            prompt = "Please make an angry comment on this statement: "+ prompt
        else:
            prompt = "Pleas make a comment on this statement: "+ prompt

        # Define the API key and the endpoint URL
        api_key = API_KEY
        model = "text-davinci-003"
        # url = f"https://api.openai.com/v1/engines/{model}/jobs"  depreciated
        url = "https://api.openai.com/v1/completions"
        

        # Define the headers for the API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # Define the data for the API request
        data = {
            "prompt": prompt,
            "model": model,
            "temperature": 0.9,
            "top_p": 1,
            "max_tokens": 100,
            "n":1
        }

        # Send the API request
        # logger.info(f"prompt is: {prompt}")
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Error accessing OpenAI API, status code: {response.status_code}")

        # Extract the text generated by the API
        result = response.json()
        generated_text = result['choices'][0]['text']

        # Log a message indicating that text generation was successful
        logger.info(f"Generated text: {generated_text}")

        # Return the generated text
        return generated_text, 200

    except Exception as e:
        # Log an error message if an exception was raised
        logger.error(f"Error generating text: {str(e)}")

        # Return a 500 Internal Server Error response
        return "Error generating text", 500

if __name__ == "__main__":
    app.run()