# Use the official Python image as the base
FROM python:3.12

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt to the container
COPY ./requirements.txt /code/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the entire app directory into the container
COPY ./app /code/app

# Expose the port the app will run on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
