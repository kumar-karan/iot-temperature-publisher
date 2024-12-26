import pandas as pd
from datetime import datetime, timedelta
import random

start_time = datetime.now()
rows = 1000  # Number of rows

data = {
    "Timestamp": [(start_time + timedelta(seconds=i * 5)).strftime("%Y-%m-%d %H:%M:%S") for i in range(rows)],
    "Temperature": [round(random.uniform(20.0, 30.0), 2) for _ in range(rows)]
}

df = pd.DataFrame(data)
df.to_csv("data/temperature_data.csv", index=False)
print("CSV File Generated: data/temperature_data.csv")
