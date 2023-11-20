# Use the base image: Python 3.11
FROM python:3.11

# Create a directory in the image
RUN mkdir -p /home/app

# Set the working dir
WORKDIR /home/app

# Prevent Python from writing bytecode files (.pyc files) to disk. Not needed when
# building images.
ENV PYTHONDONTWRITEBYTECODE 1

# In a Docker container or similar environments, unbuffered mode can help ensure
# that output from Python applications is immediately visible in the container logs,
# making troubleshooting and monitoring easier.
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Copy all files on current dir and sub dirs to the container image's /home/app/ dir
COPY . /home/app/

# Install requirements
RUN pip install -r requirements.txt

# Setting the exposed port
EXPOSE 8000

# Run the command when container is run
CMD python manage.py runserver 0.0.0.0:8000
