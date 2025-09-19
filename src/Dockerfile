#Intstructions go here if you don't know what to do

FROM python:3.11-slim

WORKDIR /app

# Copy your Python script and JSON file
COPY . .

RUN pip install flask

# Run your Python app
CMD ["python", "app.py"]