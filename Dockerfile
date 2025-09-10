    # Use an official lightweight Python image as the base image
    FROM python:3.12-slim

    # Set the working directory inside the container
    WORKDIR /
    # Copy the requirements.txt file into the container
    COPY requirements.txt .
    RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*
    # Install the Python dependencies
    RUN pip install --no-cache-dir -r requirements.txt
    RUN pip uninstall -y opencv-python && pip install --no-cache-dir opencv-python-headless
    # Copy the rest of your Flask application code into the container
    COPY . .

    # Expose the port your Flask application will run on (e.g., 5000)
    EXPOSE 8000

    # Command to run your Flask application when the container starts
    CMD ["python", "app.py"]