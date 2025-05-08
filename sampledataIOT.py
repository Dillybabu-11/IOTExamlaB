import time
import json
import random
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=IoTHubMQTT.azure-devices.net;DeviceId=myDevice;SharedAccessKey=HakOlv+xJRwVtZeir8BaVfaG0hW0kBfMYnIJWUnjCxk="

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_telemetry():
    while True:
        data = {
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "humidity": round(random.uniform(30.0, 50.0), 2),
            "asset_id": "Machine_1",
            "timestamp": time.time()
        }
        message = Message(json.dumps(data))
        client.send_message(message)
        print(f"Sent: {data}")
        time.sleep(5)  # Send data every 5 seconds

try:
    send_telemetry()
except KeyboardInterrupt:
    client.shutdown()
