# Use a base image with Python installed
FROM python:3.11.3-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and model files to the container
COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y gcc python3-dev

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy rest of assets
COPY src/ ./src/
COPY ./model/git-base-textcaps ./model/git-base-textcaps

WORKDIR /app/src

# Set the command to run your script when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
