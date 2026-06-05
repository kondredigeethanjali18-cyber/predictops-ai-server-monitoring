import pandas as pd

df = pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")

features = [
    "CPU_Usage_Percent",
    "Memory_Usage_MB",
    "Disk_Usage_Percent",
    "Failed_Transactions",
    "Retry_Count",
    "Alert_Count",
    "Error_Count",
    "Failure"
]

failure_conditions = (
    (df["CPU_Usage_Percent"] > 80)
    | (df["Memory_Usage_MB"] > 15000)
    | (df["Disk_Usage_Percent"] > 90)
    | (df["Failed_Transactions"] > 30)
    | (df["Severity"] == "High")
)

df["Failure"] = failure_conditions.astype(int)


X = df[features]     # input features
y = df["Failure"]    #target variable

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,        # 20% test data
    random_state=42,
    stratify=y            # VERY IMPORTANT for imbalanced data
)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(class_weight="balanced")
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#confusion matrix

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

