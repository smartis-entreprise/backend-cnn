# Use a base image with tensorflow and python3
FROM tensorflow/tensorflow:2.4.0-gpu-jupyter

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code into the container
COPY . .

# Command to run when the container starts
CMD ["python", "app.py"]
