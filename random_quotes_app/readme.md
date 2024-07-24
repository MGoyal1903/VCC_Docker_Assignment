# Docker Assignment
This is assignment project for virtualization and cloud computing.
    # objective - Create a docker image of web application and deploy and run inside the container.

# Random Quotes Flask App

## Description

The Random Quotes Flask App is a simple web application built using Flask and Docker. This app displays a random inspirational quote each time the page is refreshed. The quotes are pre-defined and selected randomly to provide a refreshing user experience. 

The app uses Docker for containerization, making it easy to deploy and run consistently across different environments.

## Features

- Displays a random quote from a predefined list each time the page is refreshed.
- Simple and clean user interface with a button to reload the quote.
- Containerized using Docker for consistent deployment.

## Step-by-Step Development and Deployment

1. Set Up Your Development Environment
    1.1. Install Prerequisites
    -**Python**: Install Python 3.9 or later. You can download it from [Python's official website](https://www.python.org/downloads/).
    - **Docker**: Install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).

2. Create the Flask Application
    2.1. Set Up a Project Directory

3. Containerize the Application with Docker
    3.1. Create a Dockerfile in the root of your project directory, create a file named Dockerfile
    3.2. Create the Requirements File

4. Build and Run the Docker Container
    4.1. Build the Docker Image build the Docker image with the following command:
    ## docker build -t random-quotes-app .
    4.2. Run the Docker Container run the Docker container, mapping port 5000 of the container to port 5000 on your host:
    ## docker run -p 5000:5000 random-quotes-app

5. Access the Application Open your web browser and go to http://localhost:5000. You should see the Random Quotes app running. 
   Refresh the page to get a new quote.


Application Structure
app.py: Contains the Flask application logic.
Dockerfile: Docker configuration file.
requirements.txt: Python package dependencies.
templates/index.html: HTML template for rendering quotes.
static/style.css: CSS for styling the application.

Author
Mayank Goyal
Roll Number: G23AI2120
GitHub: (https://github.com/MGoyal1903)

License
This project is licensed under the MIT License - see the LICENSE file for details.