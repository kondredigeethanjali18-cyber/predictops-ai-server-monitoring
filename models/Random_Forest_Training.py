import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")

# -----------------------------
# CREATE FAILURE TARGET
# -----------------------------
failure_conditions = (
    (df["CPU_Usage_Percent"] > 80) |
    (df["Memory_Usage_MB"] > 15000) |
    (df["Disk_Usage_Percent"] > 90) |
    (df["Failed_Transactions"] > 30) )

df["Failure"] = failure_conditions.astype(int)

# -----------------------------
# FEATURES
# -----------------------------
features = [
    "CPU_Usage_Percent",
    "Memory_Usage_MB",
    "Disk_Usage_Percent",
    "Response_Time_ms",
    "Failed_Transactions",
    "Retry_Count",
    "Alert_Count",
    "Error_Count",
    "Escalation_Level"
]

X = df[features]
y = df["Failure"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# TRAIN MODEL
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


model.fit(X_train, y_train)

# -----------------------------
# EVALUATE
# -----------------------------
predictions = model.predict(X_test)

print("Accuracy :", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall   :", recall_score(y_test, predictions))
print("F1 Score :", f1_score(y_test, predictions))

# -----------------------------
# SAVE MODEL
# -----------------------------
save_path = r"C:\Users\kgeet\OneDrive\Desktop\PredictOps-AI\models\random_forest.pkl"

with open(save_path, "wb") as f:
    pickle.dump(model, f)

print("Model Saved Successfully")
print(save_path)