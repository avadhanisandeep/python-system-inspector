import subprocess
import time
from datetime import datetime

def ping_host(host="google.com"):
    print("===== Network Check =====")
    print(f"Time: {datetime.now()}")
    print(f"Pinging: {host}")
    
    try:
        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host], stderr=subprocess.STDOUT)
        latency = (time.time() - start) * 1000
        print(f"✅ Online - Latency: {latency:.2f} ms")
    except subprocess.CalledProcessError:
        print("❌ Offline or Host Unreachable")

if __name__ == "__main__":
    ping_host()
