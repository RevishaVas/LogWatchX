import json
import time
import requests

LOG_FILE = "C:\\Users\\DELL\\Documents\\LogWatchX\\applogs.log"
LOGSTASH_URL = "http://localhost:5044"

def send_to_logstash(log_entry):
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(LOGSTASH_URL, data=json.dumps(log_entry), headers=headers)
        if response.status_code != 200:
            print(f"Failed to send log: {response.text}")
    except Exception as e:
        print(f"Error sending log: {e}")

def tail_logs():
    with open(LOG_FILE, "r") as file:
        print("File opened successfully!")
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue
            log_entry = {"log": line.strip()}
            send_to_logstash(log_entry)

if __name__ == "__main__":
    tail_logs()
