# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8000 for FastAPI
EXPOSE 8080