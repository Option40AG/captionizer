# Use a base image with Python installed
FROM python:3.11.3 as builder

WORKDIR /app

# Copy the Python script and model files to the container
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --user --no-cache-dir --upgrade -r requirements.txt

# Copy rest of assets
COPY src/ ./src/
COPY ./model/git-base-textcaps ./model/git-base-textcaps

# Take slim python image
FROM python:3.11.3-slim

# Copy installed python modules
COPY --from=builder /root/.local /root/.local

# Add them to the PATH
ENV PATH=/root/.local/bin:$PATH

# Copy everything to the app directory
COPY . /app

WORKDIR /app/src

# Set the command to run your script when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]