# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for psutil
RUN apt-get update && apt-get install -y gcc python3-dev

# Install the Python libraries we need
RUN pip install psutil pymongo

# Copy your monitor.py script into the container
COPY monitor.py .

# Run the script when the container starts
CMD ["python", "monitor.py"]
