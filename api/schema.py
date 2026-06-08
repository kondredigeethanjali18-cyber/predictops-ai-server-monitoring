from pydantic import BaseModel

class PredictRequest(BaseModel):
    CPU_Usage_Percent: float
    Memory_Usage_MB: float
    Disk_Usage_Percent: float
    Response_Time_ms: float
    Failed_Transactions: int
    Retry_Count: int
    Alert_Count: int
    Error_Count: int
    Escalation_Level: int