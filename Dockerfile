# Use a base image with tensorflow and python3
FROM tensorflow/tensorflow:latest

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copy the code into the container
COPY . .

# Command to run when the container starts
CMD ["python", "app.py"]
