from fastapi import FastAPI
from schema import PredictRequest
import pandas as pd
import joblib
import traceback

app = FastAPI(
    title="PredictOps AI API",
    description="Predictive Maintenance API using Random Forest",
    version="1.0"
)

# Load trained model
MODEL_PATH = r"C:\Users\kgeet\OneDrive\Desktop\PredictOps-AI\models\random_forest.pkl"

model = joblib.load(MODEL_PATH)

print("Model Loaded Successfully")
print("Features Expected By Model:")
print(model.feature_names_in_)


@app.get("/")
def home():
    return {
        "message": "PredictOps AI API is Running Successfully"
    }


@app.post("/predict")
def predict(data: PredictRequest):

    try:

        input_df = pd.DataFrame([{
            "CPU_Usage_Percent": data.CPU_Usage_Percent,
            "Memory_Usage_MB": data.Memory_Usage_MB,
            "Disk_Usage_Percent": data.Disk_Usage_Percent,
            "Response_Time_ms": data.Response_Time_ms,
            "Failed_Transactions": data.Failed_Transactions,
            "Retry_Count": data.Retry_Count,
            "Alert_Count": data.Alert_Count,
            "Error_Count": data.Error_Count,
            "Escalation_Level": data.Escalation_Level
        }])

        prediction = model.predict(input_df)[0]

        probs = model.predict_proba(input_df)[0]

        confidence = probs.max()

        return {
            "prediction": int(prediction),
            "status": "Failure Expected" if prediction == 1 else "Healthy System",
            "confidence_score": round(float(confidence), 4),
            "healthy_probability": round(float(probs[0]), 4),
            "failure_probability": round(float(probs[1]), 4)
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "error": str(e)
        }