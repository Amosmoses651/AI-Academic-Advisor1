
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse

app = FastAPI(title="AI-Powered Academic Advisor")

# Look for the trained model in this project's folder
MODEL_PATH = Path(__file__).parent / "academic_advisor_model.pkl"

model = None

if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)


class StudentData(BaseModel):
    gpa: float = Field(ge=0, le=5)
    attendance: float = Field(ge=0, le=100)
    study_hours: float = Field(ge=0, le=24)
    failed_courses: int = Field(ge=0)


@app.get("/")
def home():
    return FileResponse(
        Path(__file__).parent / "index.html"
    )


@app.get("/health")
def health():
    return {
        "message": "Academic Advisor API is running!",
        "model_loaded": model is not None,
    }


@app.post("/predict")
def predict(student: StudentData):
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Trained model not found. Train the model first.",
        )

    student_data = pd.DataFrame([{
        "gpa": student.gpa,
        "attendance": student.attendance,
        "study_hours": student.study_hours,
        "failed_courses": student.failed_courses,
    }])

    prediction = str(model.predict(student_data)[0])

    advice = {
        "Low": "Maintain your study habits and keep revising.",
        "Moderate": "Revise difficult topics and practise past questions.",
        "High": "Create a study timetable and seek academic support.",
    }

    return {
        "predicted_support_level": prediction,
        "recommendation": advice.get(
            prediction,
            "Consult your academic adviser.",
        ),
    }
