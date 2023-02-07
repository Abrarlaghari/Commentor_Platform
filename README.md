# Commentor_Platform
This repository contains the text generation API for Commenter Platform 

## API README
# Endpoint Description
This API endpoint provides functionality to generate the comments based on the prompt.

# Endpoints
The following endpoints are available:

# POST /gpt3
Description
This endpoint allows you to generate comment using OpenAI GPT-3 completion endpoint.

Parameters
The following parameters are required in a POST request to this endpoint:

prompt (string): Linked/facebook/twitter post for which reponse will be generated.
keywords (array(list) of string) (optional): Keywords based on which response will be generated.
emotions (string): Type of the response. It can be sarcastic, funny, serious, provocative ,creative (defult)
platform (string): The platform can be facebook, linkedin or twitter. It determines the length of the reponse.

Example
To get a reponse using this POST api following curk command can be used:

curl -X POST "http://127.0.0.1:5000/gpt3" -H "Content-Type: application/json" -d '{
    "prompt": "I am changing my job.",
    "keywords":["excited", "nervous"],
    "emotion":"funny",
    "platform": "facebook"

}'
