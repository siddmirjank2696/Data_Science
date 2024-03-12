# Downloading a Python 3.7 docker image
FROM python:3.7

# Copying all files from the root to the application folder
COPY . /app

# Specifying the current working directory (application folder)
WORKDIR /app

# Updating the package files on the system
RUN apt update -y

# Installing the dependencies needed to run the application
RUN pip install -r requirements.txt

# Executing the application using python app.py command
CMD ["python3", "app.py"]