from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pickle
import numpy as np
import os
import csv

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "best_model.pkl")
csv_path = os.path.join(BASE_DIR, "..", "..", "Dataset", "diabetes.csv")
html_path = os.path.join(BASE_DIR, "..", "..", "Frontend", "index.html")

with open(model_path, "rb") as f:
    model = pickle.load(f)


def save_to_csv(user_input: "UserInput", prediction: float):
    file_exists = os.path.exists(csv_path)
    with open(csv_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'])
        writer.writerow([
            user_input.Pregnancies,
            user_input.Glucose,
            user_input.BloodPressure,
            user_input.SkinThickness,
            user_input.Insulin,
            user_input.BMI,
            user_input.DiabetesPedigreeFunction,
            user_input.Age,
            int(prediction)
        ])


class UserInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


@app.post("/predict")
async def predict(user_input: UserInput):
    try:
        input_data = np.array([
            user_input.Pregnancies,
            user_input.Glucose,
            user_input.BloodPressure,
            user_input.SkinThickness,
            user_input.Insulin,
            user_input.BMI,
            user_input.DiabetesPedigreeFunction,
            user_input.Age
        ]).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        save_to_csv(user_input, prediction)
        return {"prediction": float(prediction)}
    except Exception as e:
        return {"error": str(e)}


@app.get("/", response_class=HTMLResponse)
async def root():
    with open(html_path, "r") as f:
        return f.read()
