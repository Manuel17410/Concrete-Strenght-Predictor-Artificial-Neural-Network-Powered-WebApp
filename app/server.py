import joblib
import numpy as np
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

# Load the trained model and scaler
model = joblib.load('app/model_3.joblib')
scaler = joblib.load('app/scaler.joblib')

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Serve static files (if any, like CSS, JS, or images)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    """
    Render the prediction form.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    cement: float = Form(...),
    blast_furnace_slag: float = Form(...),
    fly_ash: float = Form(...),
    water: float = Form(...),
    superplasticizer: float = Form(...),
    coarse_aggregate: float = Form(...),
    fine_aggregate: float = Form(...),
    age: int = Form(...),
):
    """
    Handle prediction requests and return the result.
    """
    # Prepare the input features for prediction
    input_features = np.array([
        cement, blast_furnace_slag, fly_ash, water, 
        superplasticizer, coarse_aggregate, fine_aggregate, age
    ]).reshape(1, -1)

    # Scale the features
    scaled_features = scaler.transform(input_features)

    # Predict the strength
    prediction = model.predict(scaled_features)[0]

    # Render the prediction result on the same page
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": round(float(prediction), 2),  # Round to 2 decimal places
        },
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)







