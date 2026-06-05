import pandas as pd
import numpy as np

data =pd.read_csv("Dataset/logging_monitoring_anomalies.csv")
print("First 5 rows of the dataset: ")
print(data.head())

print("\nDataset Information:")
print(data.info())


print("\nSummary Statistics: ")
print(data.describe())

print("\n Dataset Shape:")
print(data.shape)
print("\n Missing Values: ")
print(data.isnull().sum())

#convert severity to binary target

data["failure"] = data["Severity"].apply(lambda x:1 if x== "High" else 0)
print(data["failure"].value_counts())


#keeping only useful columns

features = [ "CPU_Usage_Percent","Memory_Usage_MB",
            "Disk_Usage_Percent",
            "Network_In_KB",
            "Network_Out_KB",
            "Response_Time_ms",
            "Resolution_Time_min",
            "Login_Attempts",
            "Failed_Transactions",
            "Alert_Count",
            "Retry_COunt",
            "Anomaly_Duration_sec",
            "Affected_Services",
            "Patch_Level",
            "Escalation_Level"]
x = data["CPU_Usage_Percent"]
y = data["failure"]

print("X shape: ", x.shape )
print("y shape: ", y.shape)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42,
                                                    stratify=y)

print("Training data: ", x_train.shape)
print("Testing data: ", x_test.shape)

