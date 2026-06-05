import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load dataset

df= pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")

#select only required columns

selected_features = ["CPU_Usage_Percent",
            "Memory_Usage_MB", 
            "Disk_Usage_Percent", 
            "Failed_Transactions", 
            "Retry_Count", 
            "Alert_Count", 
            "Error_Count"]

heatmap_data = df[selected_features]

#Calculate correlation matrix

correlation_matrix = heatmap_data.corr()

#Plot heatmap

plt.figure(figsize=(12,8))

sns.heatmap(correlation_matrix,
            annot=True,
            cmap="YlGnBu", 
            fmt=".2f", linewidths=0.5)
plt.title("Predictops AI Feature Correlation Heatmap")
plt.show()
