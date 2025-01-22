import joblib
import numpy as np
from fastapi import FastAPI
import uvicorn

# trained neural network model and scaler
model = joblib.load('app/model_3.joblib')
scaler = joblib.load('app/scaler.joblib')

app = FastAPI()

@app.get('/')
def read_root():

    """
    Root endpoint to verify the API is running.
    """

    return {'message': 'Concrete Compressive Strength Prediction API.2'}

@app.post('/predict')
def predict(data: dict):
    """
    Predicts the compressive strength of concrete based on input features.

    Args:
        data (dict): A dictionary containing the features to predict.
        Example: 
        {
            "features": {
                "Cement (component 1)(kg in a m^3 mixture)": 540.0,
                "Blast Furnace Slag (component 2)(kg in a m^3 mixture)": 0.0,
                "Fly Ash (component 3)(kg in a m^3 mixture)": 0.0,
                "Water  (component 4)(kg in a m^3 mixture)": 162.0,
                "Superplasticizer (component 5)(kg in a m^3 mixture)": 2.5,
                "Coarse Aggregate  (component 6)(kg in a m^3 mixture)": 1040.0,
                "Fine Aggregate (component 7)(kg in a m^3 mixture)": 676.0,
                "Age (day)": 28
            }
        }
        
    Returns:
        dict: A dictionary containing the predicted compressive strength
    """

    # Print the keys of the features dictionary to inspect the available keys
    print(data['features'].keys())

    # Extract features from the input data
    input_features = [
        data['features']['Cement (component 1)(kg in a m^3 mixture)'],
        data['features']['Blast Furnace Slag (component 2)(kg in a m^3 mixture)'],
        data['features']['Fly Ash (component 3)(kg in a m^3 mixture)'],
        data['features']['Water  (component 4)(kg in a m^3 mixture)'],
        data['features']['Superplasticizer (component 5)(kg in a m^3 mixture)'],
        data['features']['Coarse Aggregate  (component 6)(kg in a m^3 mixture)'],
        data['features']['Fine Aggregate (component 7)(kg in a m^3 mixture)'],
        data['features']['Age (day)']
    ]

    # Extract features from the input data
    features = np.array(input_features).reshape(1, -1)  # Ensure it's in the correct shape

    # Scale the input features using the same scaler used during training
    scaled_features = scaler.transform(features)
    
    # Make the prediction using the model
    prediction = model.predict(scaled_features)[0]
    
    # Since the prediction is a continuous value (for regression), return it directly
    return {'predicted_strength': float(prediction)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



