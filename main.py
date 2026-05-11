import sys
import random
import time
import datetime

current_time = datetime.datetime.now()

print("\n|DASHBOARD|")
print(current_time.strftime("%Y-%m-%d %H:%M:%S"))

while True:
    print("\n-Select an option-")
    print("[1] Wifi jammer")
    print("[0] Exit")

    option_chosen = input("\nSelect an option: ")

    try:
        option_chosen = int(option_chosen)
    except ValueError:
        print("[E] Please enter an integer")
        continue

    if option_chosen == 0:
        print("goodbye")
        sys.exit(0)
    elif option_chosen == 1:
        print("Wifi jammer selected")
