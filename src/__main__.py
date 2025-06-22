from system_info import get_system_info
from network_check import ping_host

def main():
    print("📊 Python System Inspector")
    print("1. View System Info")
    print("2. Check Network Status")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        get_system_info()
    elif choice == "2":
        ping_host()
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
