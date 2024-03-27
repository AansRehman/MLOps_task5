# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install Flask and pymongo
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask pymongo flask_cors

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
