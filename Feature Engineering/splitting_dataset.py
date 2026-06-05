import pandas as pd
import numpy as np

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
x = data[features]
y = data["failure"]




#splitting dataset into train and test sets

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42,
                                                    stratify=y
                                                    )
print("Training data: ", x_train)
print("Testingdata:", x_test)


# print("Training data: ", x_train.shape)
# print("Testing data: ", x_test.shape)

print("\nTraining set class distribution:")
print(y_train.value_counts())
print("\nTesting set class distribution:")
print(y_test.value_counts())
