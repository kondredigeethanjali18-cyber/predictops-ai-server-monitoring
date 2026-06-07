import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

df = pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")

feature_names = [
    "CPU_Usage_Percent",
    "Memory_Usage_MB",
    "Disk_Usage_Percent",
    "Failed_Transactions",
    "Retry_Count",
    "Alert_Count",
    "Error_Count"
]

failure_conditions = (
    (df["CPU_Usage_Percent"] > 80)
    | (df["Memory_Usage_MB"] > 15000)
    | (df["Disk_Usage_Percent"] > 90)
    | (df["Failed_Transactions"] > 30)
    | (df["Severity"] == "High")
)

df["Failure"] = failure_conditions.astype(int)

X = df[feature_names]
y = df["Failure"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, predictions),
        "Precision": precision_score(y_test, predictions),
        "Recall": recall_score(y_test, predictions),
        "F1 Score": f1_score(y_test, predictions)
    })

results_df = pd.DataFrame(results)

print(results_df)


# Bar chart for all metrics

import matplotlib.pyplot as plt

results_df.set_index("Model")[["Accuracy", "Precision", "Recall", "F1 Score"]].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Model Performance Comparison")
plt.ylabel("Score")
plt.ylim(0, 1)
plt.xticks(rotation=360)
plt.legend(loc="lower right")
plt.show()