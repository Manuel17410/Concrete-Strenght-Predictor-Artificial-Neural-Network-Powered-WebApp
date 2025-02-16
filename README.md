# Concrete Strenght Predictor: Artificial Neural Network Powered Web-App with Docker Deployment

In this project, a fully functional website was developed using HTML, integrated with a FastAPI backend, to predict the compressive strength of concrete. The prediction model is powered by artificial neural networks (ANN) and was deployed using Docker for seamless containerization and cross-platform compatibility.

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

1 - Clone the Repository:

git clone https://github.com/Manuel17410/Concrete-Strength-Predictor-ANN-Powered-Web-App-with-Docker-Deployment.git

2 - Navigate to the Project Directory:

cd Concrete-Strength-Predictor-ANN-Powered-Web-App-with-Docker-Deployment

3 - Create and Activate a Virtual Environment (Optional but Recommended):

python -m venv venv
source venv/bin/activate  # On Linux/MacOS
venv\Scripts\activate     # On Windows

4 - Install Dependencies: Use the requirements.txt file to install the required libraries:

pip install -r requirements.txt

5 - Run the Application: Start the FastAPI application: 

uvicorn main:app --host 127.0.0.1 --port 8000

6 - Access the Web App: Open your browser and go to: 

http://127.0.0.1:8000

## Website Interface

![Example Image](image/Concrete%20Strength%20Predictor.png)

