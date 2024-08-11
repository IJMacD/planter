# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim AS final

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    dpkg --add-architecture arm64 && \
    apt-get install libusb-1.0-0

COPY ./requirements.txt requirements.txt

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY run.py .

CMD ["python", "run.py", "3"]
