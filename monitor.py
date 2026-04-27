import psutil
import time
import sys

def collect_stats():
    print("--- MONITOR STARTING ---", flush=True)
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            print(f"STATS -> CPU: {cpu}% | RAM: {ram}%", flush=True)
            time.sleep(2)
    except Exception as e:
        print(f"CRASH: {e}", flush=True)

if __name__ == "__main__":
    collect_stats()
