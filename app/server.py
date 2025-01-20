import joblib
import numpy as np
from fastapi import FastAPI
import uvicorn

# Load your trained neural network model
model = joblib.load('app/model_3.joblib')

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Concrete Compressive Strength Prediction API'}

@app.post('/predict')
def predict(data: dict):
    """
    Predicts the concrete compressive strength for a given set of features.

    Args:
        data (dict): A dictionary containing the features to predict.
        e.g. {"features": [feature1, feature2, ..., featureN]}

    Returns:
        dict: A dictionary containing the predicted concrete compressive strength.
    """
    # Extract features from the input data
    features = np.array(data['features']).reshape(1, -1)  # Ensure it's in the correct shape
    
    # Make the prediction using the model
    prediction = model.predict(features)
    
    # Since the prediction is a continuous value (for regression), return it directly
    return {'predicted_strength': prediction[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

