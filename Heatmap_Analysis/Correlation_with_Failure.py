import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load dataset

df= pd.read_csv("Dataset/Logging_Monitoring_Anomalies_Enhanced.csv")

#create failure column

df["failure"] = df["Severity"].apply(lambda x:1 if x== "High" else 0)

#select only required columns

selected_features = ["CPU_Usage_Percent",
            "Memory_Usage_MB", 
            "Disk_Usage_Percent", 
            "Failed_Transactions", 
            "Retry_Count", 
            "Alert_Count", 
            "Error_Count",
            "failure"]


correlation = df[selected_features].corr()

failure_corr = correlation[["failure"]].sort_values(by="failure",
                                                     ascending=False)

#Plot heatmap

plt.figure(figsize=(6,6))

sns.heatmap(failure_corr,
            annot=True,
            cmap="Reds", 
            fmt=".2f")
plt.title("Correlation Heatmap with Failure")
plt.show()
