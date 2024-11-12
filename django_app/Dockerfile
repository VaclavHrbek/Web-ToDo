# Use the official Python base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    nodejs  \
    npm

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . /app

# Expose the port that the Django and Vue app will run on
EXPOSE 8000 5173

# Start the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]