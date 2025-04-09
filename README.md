# Concrete Strenght Predictor: Artificial Neural Network Powered Web-App with Docker Deployment

In this project, a fully functional website was developed using HTML, integrated with a FastAPI backend, to predict the compressive strength of concrete. The prediction model is powered by artificial neural networks (ANN) and was deployed using Docker for seamless containerization and cross-platform compatibility.

## Video Demonstration of the App on YouTube

To give you a quick overview of how the app works, I’ve created a demonstration video. While setting up the app locally can take a few minutes and sometimes lead to dependency issues, this video allows you to experience the website without any setup.

[![Watch the Demo](https://img.youtube.com/vi/rNWj6oO8w_I/0.jpg)](https://youtube.com/shorts/rNWj6oO8w_I?si=R_ET-zTJvY3SbOwn)

Additionally, I am actively working on hosting the app on a cloud platform to make it even easier to access.

## How to run the website using Docker:

1- Clone the Repository:

git clone https://github.com/Manuel17410/Concrete-Strength-Predictor-ANN-Powered-Web-App-with-Docker-Deployment.git

2- Navigate to the Project Directory and open it in VSC:

cd Concrete-Strength-Predictor-ANN-Powered-Web-App-with-Docker-Deployment

3 - Install Dependencies: Use the requirements.txt file to install the required libraries: pip install -r requirements.txt

4- Build the Docker Image:

docker build -t concrete-strength-predictor .

5- Run the Docker Container:

docker run -d -p 8000:8000 concrete-strength-predictor

6- Access the Web App: Open your browser and go to:

http://127.0.0.1:8000

## How to run the website without Docker:

Follow these steps if Docker is not installed on your system:

1 - Download the repository

2 - Go to the repo folder in your computer, and open VSC (Right click, "In Terminal offnen", and then write code .)

3 - Write  -    pip install -r requirements.txt   - in the terminal

5 - Run the Application: Start the FastAPI application: 

uvicorn app.server:app --host 0.0.0.0 --port 8000

6 - Access the Web App: Open your browser and go to: 

http://127.0.0.1:8000

## Website Interface

![Example Image](image/Concrete%20Strength%20Predictor.png)

