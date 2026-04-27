print("SCRIPT IS LOADING...")
import psutil
import time
import sys

def run_test():
    print("--- SYSTEM MONITOR STARTING ---")
    # This forces the text to show up in Docker immediately
    sys.stdout.flush() 

    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            
            # --- COLOR LOGIC START ---
            GREEN = "\033[92m"
            RED = "\033[91m"
            RESET = "\033[0m"
            
            # Pick a color based on how hard the CPU is working
            color = RED if cpu > 80 else GREEN
            
            # Now we print using that color variable
            print(f"{color}STATS -> CPU: {cpu}% | RAM: {ram}%{RESET}", flush=True)
            # --- COLOR LOGIC END ---
            
            time.sleep(2)
    except Exception as e:
        print(f"CRASH ERROR: {e}")
        sys.stdout.flush()

if __name__ == "__main__":
    run_test()