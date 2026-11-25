import random
import time

print("=" * 45)
print("       🤖 ROBOT APOCALYPSE")
print("        SURVIVAL SIMULATOR")
print("=" * 45)

player = input("\nEnter your commander name: ")

battery = 100
health = 100
rescued = 0

print("\nWelcome Commander", player)
print("The robot apocalypse has begun!")
print("Your mission: SAVE THE CITY!")

while battery > 0 and health > 0:

    print("\n========== COMMAND CENTRE ==========")
    print("1. Scan the city")
    print("2. Rescue survivors")
    print("3. Recharge robot")
    print("4. Check system status")
    print("5. Exit mission")

    choice = input("\nEnter your command: ")

    if choice == "1":
        event = random.choice([
            "No enemies detected!",
            "Dangerous robot detected!",
            "Survivors found nearby!"
        ])

        print("\nSCAN RESULT:", event)
        battery -= 10

    elif choice == "2":
        rescued += random.randint(1, 5)
        battery -= 20
        print("\nRescue mission successful!")
        print("Total survivors rescued:", rescued)

    elif choice == "3":
        battery = min(100, battery + 30)
        print("\nRobot recharged!")
        print("Battery:", battery, "%")

    elif choice == "4":
        print("\nBattery:", battery, "%")
        print("Health:", health)
        print("Survivors rescued:", rescued)

    elif choice == "5":
        print("\nMission terminated.")
        break

    else:
        print("\nInvalid command!")

    if battery <= 20:
        print("\n⚠️ WARNING: LOW BATTERY!")

    if battery <= 0:
        print("\n🤖 ROBOT SHUTDOWN!")

print("\n========== MISSION REPORT ==========")
print("Commander:", player)
print("Survivors rescued:", rescued)
print("Final battery:", battery)
print("Thanks for playing!")
