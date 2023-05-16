# Use the python 3.10 slim image as a base image for this container
FROM node:19.8.1-slim

# Set the working directory to /app
WORKDIR /app

# Install PostgreSQL binaries for the psycopg python package
RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Install python 3.10
RUN apt-get install -y python3.10 python3-pip python3-venv

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install required packages in the virtual environment
RUN /opt/venv/bin/pip3 install pip --upgrade && \
    /opt/venv/bin/pip3 install -r requirements.txt

# Copy package.json and package-lock.json to the working directory
COPY package*.json .

# Install dependencies
RUN npm i

# Copy all the code from the local file system to the app directory and set it as the working directory
COPY . /app

# Activate the production server without actually activating the virtual environment
RUN chmod +x entrypoint.sh

# Running the entrypoint file to start the production server
CMD ["/app/entrypoint.sh"]
