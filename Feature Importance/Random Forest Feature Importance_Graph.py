import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")

feature_names = ["CPU_Usage_Percent",
                 "Memory_Usage_MB",
                 "Disk_Usage_Percent",
                 "Failed_Transactions",
                 "Retry_Count",
                 "Alert_Count",
                 "Error_Count",
                 "Anomaly_ID"]

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

#split dataset into train and test sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Random Forest model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

#Get feature importance

importance = model.feature_importances_
feature_importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

importance_df = (feature_importance_df.sort_values(by="Importance",
                                            ascending=False))

print(importance_df)

# Plot feature importance

plt.figure(figsize=(10,6))

plt.barh(
    importance_df["Feature"],
    importance_df["Importance"], color="skyblue")

plt.title("Feature Importance from Random Forest")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()