import random
import time

print("=" * 40)
print("     CITY DISASTER ALERT SYSTEM")
print("=" * 40)

disasters = {
    "POWER FAILURE": "City electricity has stopped!",
    "MASSIVE STORM": "Strong winds are damaging buildings!",
    "CITY FIRE": "Fire detected in residential area!",
    "RADIATION LEAK": "Dangerous radiation detected!",
    "ROBOT INVASION": "Unknown robots are attacking!"
}

print("\nScanning city for disasters...")
time.sleep(1)

for i in range(5):

    event = random.choice(list(disasters.keys()))

    print("\n🚨 DISASTER ALERT:", event)
    print(disasters[event])

    print("\nChoose your response:")
    print("1. Send rescue robots")
    print("2. Activate emergency shield")
    print("3. Ignore the warning")

    choice = input("Your decision: ")

    if choice == "1":
        print("Rescue robots dispatched!")

    elif choice == "2":
        print("Emergency shield activated!")

    elif choice == "3":
        print("Warning ignored! City risk increased!")

    else:
        print("Invalid response!")

    print("-" * 40)

print("\nDISASTER REPORT COMPLETE!")
print("City monitoring system activated.")
