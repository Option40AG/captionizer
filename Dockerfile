# Use a base image with Python installed
FROM python:3.11.3 as Base

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and model files to the container
COPY requirements.txt ./requirements.txt
COPY src/ ./src
COPY model/git-base-textcaps ./model/git-base-textcaps

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Use Alpine image and copy assets
FROM python:3.11.3-alpine as Slim

# Copy rest of assets
COPY --from=Base /app /app

WORKDIR /app/src

# Set the command to run your script when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
