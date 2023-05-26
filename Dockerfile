FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "app.main:app", "-b", "0.0.0.0:5000", "-c", "gunicorn.config.py", "-k", "gthread", "--worker-tmp-dir", "/dev/shm"]
