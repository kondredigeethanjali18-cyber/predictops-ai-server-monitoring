import pickle
#load model
model = pickle.load(open("random_forest_model.pkl", "rb"))

#get values from user

cpu = float(input("Enter CPU Usage Percent: "))
memory = float(input("Enter Memory Usage in MB: "))
disk = float(input("Enter Disk Usage Percent: "))
response_time = float(input("Enter Response Time in ms: "))
failed_transactions = int(input("Enter number of Failed Transactions: "))
alert_count = int(input("Enter number of Alerts: "))
error_count = int(input("Enter number of Errors: "))
retry_count = int(input("Enter number of Retries: "))
escalation_level = int(input("Enter Escalation Level: "))

#make prediction
result = model.predict([[
    cpu,
    memory,
    disk, 
    response_time,
    failed_transactions, 
    alert_count,
    error_count,
    retry_count,
    escalation_level]])

#Display result

if result[0] == 1:
    print("Prediction:High Severity Failure")
else:
    print("Prediction:Server Healthy")
