import boto3
import json
import random
import time
from datetime import datetime

# AWS region and stream
REGION_NAME = "ap-southeast-2"
STREAM_NAME = "temperature-stream"

# Initialise Kinesis client
kinesis = boto3.client("kinesis", region_name=REGION_NAME)

def generate_temperature_event():
    return {
        "device_id": f"device-{random.randint(1, 5)}",
        "temperature": round(random.uniform(20, 80), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    event = generate_temperature_event()
    print("Sending event:", event)

    kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(event),
        PartitionKey=event["device_id"]
    )

    time.sleep(1)  # simulate 1-second interval
