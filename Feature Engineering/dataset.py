import pandas as pd
import numpy as np

data =pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")
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


