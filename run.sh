#!/bin/bash

docker build -t flask_app .
docker run --rm -p 8000:8000 flask_app