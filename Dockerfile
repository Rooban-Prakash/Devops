# Use an official Python runtime as a base image
FROM python:3.9-slim

EXPOSE 80
# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application (replace with your app's entry point)
CMD ["python", "app.py"]
