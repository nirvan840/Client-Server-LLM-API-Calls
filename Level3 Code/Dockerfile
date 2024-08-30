# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 of the container available to the world outside this container
EXPOSE 80

# When output is unbuffered, Python writes each piece of data (like the result of a print() statement) to the terminal or log file immediately, without waiting to gather more data.
ENV PYTHONUNBUFFERED=1

# Run .py file when the container launches
CMD ["python", "main_v2.py"]