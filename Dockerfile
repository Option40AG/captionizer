# Use a base image with Python installed
FROM python:3.11.3-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and model files to the container
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy rest of assets
COPY src/main.py ./src/main.py
COPY ./model/git-base-textcaps ./model/git-base-textcaps

# Set the command to run your script when the container starts
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
