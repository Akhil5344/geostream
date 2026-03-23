import time
import json
import os
from google.cloud import pubsub_v1

# Config from Environment Variables (GKE ConfigMaps)
project_id = os.getenv("PROJECT_ID")
topic_id = "vehicle-telemetry"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def simulate_fleet():
    while True:
        data = {
            "vehicle_id": "truck-001",
            "lat": 34.0522,
            "lng": -118.2437,
            "timestamp": time.time()
        }
        message = json.dumps(data).encode("utf-8")
        publisher.publish(topic_path, message)
        print(f"Published: {data}")
        time.sleep(5)

if __name__ == "__main__":
    simulate_fleet()
