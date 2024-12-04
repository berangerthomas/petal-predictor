from fastapi import FastAPI
import joblib
from pydantic import BaseModel

# Charger le modèle pré-entraîné
model = joblib.load("model.joblib")

app = FastAPI()


class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Fonctions
@app.get("/")
async def root():
    return {"message": "Please use the /predict endpoint for predictions"}


@app.post("/predict")
def predict(features: IrisFeatures):
    try:
        # Convert input features to list
        input_data = [
            [
                features.sepal_length,
                features.sepal_width,
                features.petal_length,
                features.petal_width,
            ]
        ]

        # Make prediction
        prediction = model.predict(input_data)

        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
