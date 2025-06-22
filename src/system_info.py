import psutil
import platform
from datetime import datetime

def get_system_info():
    print("===== System Information Report =====")
    print(f"Date & Time: {datetime.now()}")
    print(f"System: {platform.system()} {platform.release()}")
    print()

    print("💻 CPU Info:")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"Logical CPUs: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print()

    print("🧠 Memory Info:")
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Used: {mem.used / (1024 ** 3):.2f} GB")
    print(f"Available: {mem.available / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {mem.percent}%")
    print()

    print("💽 Disk Info:")
    disk = psutil.disk_usage('/')
    print(f"Total: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Used: {disk.used / (1024 ** 3):.2f} GB")
    print(f"Free: {disk.free / (1024 ** 3):.2f} GB")
    print(f"Disk Usage: {disk.percent}%")

if __name__ == "__main__":
    get_system_info()
