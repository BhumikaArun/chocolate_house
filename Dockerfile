# Use Python 3.10 image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local code into the container's working directory
COPY . /app

# Install the required dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

