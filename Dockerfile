# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install the virtualenv package
RUN pip install virtualenv

# Create a virtual environment
RUN virtualenv venv

# Activate the virtual environment and install dependencies
RUN ./venv/bin/pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Set the environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=band.settings

# Expose the port that your Django app will run on (default is 8000)
EXPOSE 8000

# Run the Django development server
CMD ["./venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]