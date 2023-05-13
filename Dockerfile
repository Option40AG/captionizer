# Use a base image with Python installed
FROM python:3.11.3

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and model files to the container
COPY requirements.txt ./requirements.txt
COPY src/main.py ./src/main.py
COPY ./models/git-base-textcaps ./models/git-base-textcaps

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Set the command to run your script when the container starts
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
