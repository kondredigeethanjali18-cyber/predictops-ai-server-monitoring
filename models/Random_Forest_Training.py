import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

#read csv file

data =pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")


#convert severity to binary target

data["failure"] = data["Severity"].apply(lambda x:1 if x== "High" else 0)
print(data["failure"].value_counts())

#keeping only useful columns

features = [ "CPU_Usage_Percent",
            "Memory_Usage_MB",
            "Disk_Usage_Percent",
            "Response_Time_ms",
            "Failed_Transactions",
            "Alert_Count",
            "Error_Count",
            "Retry_Count",
            "Escalation_Level"]
X= data[features]

y= data["failure"]

#splitting dataset into train and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=42,
                                                    stratify=y)

model = RandomForestClassifier(n_estimators=100,
                                random_state=42)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy;", accuracy)



# Saving the model

import pickle
import os

# Absolute path to Streamlit Dashboard folder
save_path = r"C:\Users\kgeet\OneDrive\Desktop\PredictOps-AI\Streamlit Dashboard\random_forest_model.pkl"

with open(save_path, "wb") as f:
    pickle.dump(model, f)

print("Model Saved at:", save_path)

