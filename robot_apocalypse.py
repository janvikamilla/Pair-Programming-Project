import random

print("=" * 45)
print("       ROBOT APOCALYPSE")
print("        CITY EXPLORATION")
print("=" * 45)

player = input("\nEnter commander name: ")

battery = 100
health = 100
rescued = 0
enemies_defeated = 0

locations = {
"1": "Hospital",
"2": "Shopping Mall",
"3": "Research Lab",
"4": "Power Station"
}

while battery > 0 and health > 0 and rescued < 10:

print("\n========== COMMAND CENTRE ==========")
print("1. Explore City")
print("2. Rescue Survivors")
print("3. Attack Enemy")
print("4. Repair Robot")
print("5. System Status")
print("6. Exit Mission")

choice = input("\nEnter command: ")

if choice == "1":
    print("\nAVAILABLE LOCATIONS:")

    for key, location in locations.items():
        print(key + ".", location)

    zone = input("\nChoose location: ")

    if zone in locations:
        print("\nExploring:", locations[zone])
        battery -= 10

        event = random.choice(["enemy", "safe", "survivor"])

        if event == "enemy":
            print("WARNING! Enemy robot detected!")
            health -= 15

        elif event == "safe":
            print("Area secured successfully!")

        else:
            print("Survivors discovered!")
            rescued += 2

    else:
        print("Invalid location!")

elif choice == "2":
    battery -= 15
    people = random.randint(1, 3)
    rescued += people
    print("Survivors rescued:", people)

elif choice == "3":
    battery -= 10

    if random.choice([True, False]):
        enemies_defeated += 1
        print("Enemy destroyed!")

    else:
        health -= 20
        print("Enemy counterattack!")
        
elif choice == "4":
    if battery >= 10:
        health = min(100, health + 30)
        battery -= 10
        print("Robot repaired!")

    else:
        print("Not enough battery!")

elif choice == "5":
    print("\nCOMMANDER:", player)
    print("Battery:", battery, "%")
    print("Health:", health, "%")
    print("Survivors:", rescued)
    print("Enemies defeated:", enemies_defeated)

elif choice == "6":
    print("Mission abandoned!")
    break

else:
    print("Invalid command!")

if battery <= 20:
    print("\nLOW BATTERY WARNING!")

if health <= 20:
    print("\nCRITICAL HEALTH WARNING!")

if rescued >= 10:
print("\n🏆 CITY RESCUE SUCCESSFUL!")

elif health <= 0:
print("\nROBOT DESTROYED!")

elif battery <= 0:
print("\nROBOT SHUTDOWN!")

print("\n========== FINAL REPORT ==========")
print("Commander:", player)
print("Survivors rescued:", rescued)
print("Enemies defeated:", enemies_defeated)
print("Final battery:", battery)
print("Final health:", health)
