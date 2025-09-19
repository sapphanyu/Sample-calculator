#Intstructions go here if you don't know what to do

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
# Copy your Python script and JSON file
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run your Python app
CMD ["python", "app.py"]