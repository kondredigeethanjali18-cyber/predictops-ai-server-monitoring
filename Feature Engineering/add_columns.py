import pandas as pd

#load csv file
df=pd.read_csv("Dataset/server_monitoring_failure_prediction.csv")

print("Dataset Loaded Successfully")
print("Rows:",len(df))

#Create Error Count Column
df["Error_Count"]= (df["Failed_Transactions"] + df["Retry_Count"] + df["Alert_Count"])

# Create Failure column based on conditions
failure_conditions = (
    (df["CPU_Usage_Percent"] > 80)
    | (df["Memory_Usage_MB"] > 15000)
    | (df["Disk_Usage_Percent"] > 90)
    | (df["Failed_Transactions"] > 30)
    | (df["Severity"] == "High")
)

df["Failure"] = failure_conditions.astype(int)


# Save new CSV file
df.to_csv("Logging_Monitoring_Anomalies_Enhanced.csv", index=False)
print("New CSV file with added columns saved successfully")
print("File Name: Logging_Monitoring_Anomalies_Enhanced.csv")



print(df[["Error_Count", "Failure"]].head())