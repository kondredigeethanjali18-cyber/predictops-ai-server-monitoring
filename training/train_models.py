import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# -----------------------------
# 1. LOAD DATA
# -----------------------------
df = pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")

# -----------------------------
# 2. CREATE TARGET COLUMN
# -----------------------------
failure_conditions = (
    (df["CPU_Usage_Percent"] > 80) |
    (df["Memory_Usage_MB"] > 15000) |
    (df["Disk_Usage_Percent"] > 90) |
    (df["Failed_Transactions"] > 30) |
    (df["Severity"] == "High")
)

df["Failure"] = failure_conditions.astype(int)

# -----------------------------
# 3. FEATURES AND TARGET
# -----------------------------
feature_names = [
    "CPU_Usage_Percent",
    "Memory_Usage_MB",
    "Disk_Usage_Percent",
    "Failed_Transactions",
    "Retry_Count",
    "Alert_Count",
    "Error_Count"
]

X = df[feature_names]
y = df["Failure"]

# -----------------------------
# 4. TRAIN-TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# 5. MODELS
# -----------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(random_state=42)
}

# -----------------------------
# 6. TRAIN + EVALUATE
# -----------------------------
results = []

for name, model in models.items():
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # probability for ROC-AUC
    y_proba = model.predict_proba(X_test)[:, 1]

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1 Score": f1_score(y_test, y_pred),
        "ROC-AUC": roc_auc_score(y_test, y_proba)
    })

# -----------------------------
# 7. RESULTS TABLE
# -----------------------------
results_df = pd.DataFrame(results)

print("\n📊 MODEL COMPARISON RESULTS:\n")
print(results_df.sort_values(by="ROC-AUC", ascending=False))

# -----------------------------
# 8. SELECT BEST MODEL
# -----------------------------
best_model_row = results_df.sort_values(by="ROC-AUC", ascending=False).iloc[0]

best_model_name = best_model_row["Model"]
best_model = models[best_model_name]

print("\n🏆 BEST MODEL:", best_model_name)

# -----------------------------
# 9. SAVE BEST MODEL
# -----------------------------
with open("models/best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print("\n💾 Best model saved in models/best_model.pkl")

results_df.to_csv("Streamlit Dashboard/pages/outputs/results.csv", index=False)