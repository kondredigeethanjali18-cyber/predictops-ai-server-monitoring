import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

xgb_model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42,
    use_label_encoder=False,
    eval_metric="logloss"
)

df = pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")

feature_names = ["CPU_Usage_Percent",
                 "Memory_Usage_MB",
                 "Disk_Usage_Percent",
                 "Failed_Transactions",
                 "Retry_Count",
                 "Alert_Count",
                 "Error_Count"]

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


xgb_model.fit(X_train, y_train)

predictions = xgb_model.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, predictions)
print("XGBoost Accuracy:", accuracy)


#Saving the model

import pickle

pickle.dump(
    xgb_model,
    open("xgboost_model.pkl", "wb")
)

print("Model Saved")
