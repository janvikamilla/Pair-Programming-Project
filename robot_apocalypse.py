import random

print("=" * 45)
print("       ROBOT APOCALYPSE")
print("        SURVIVAL MODE")
print("=" * 45)

player = input("\nEnter commander name: ")

battery = 100
health = 100
rescued = 0
enemies_defeated = 0

while battery > 0 and health > 0 and rescued < 10:

    print("\n========== COMMAND CENTRE ==========")
    print("1. Scan for enemies")
    print("2. Rescue survivors")
    print("3. Attack enemy")
    print("4. Repair robot")
    print("5. System status")
    print("6. Exit mission")

    choice = input("\nEnter command: ")

    if choice == "1":
        print("\nScanning city...")
        battery -= 5

        if random.choice([True, False]):
            print("WARNING! Enemy detected!")
            health -= 10
        else:
            print("Area is safe!")

    elif choice == "2":
        print("\nStarting rescue mission...")
        battery -= 15

        people = random.randint(1, 3)
        rescued += people

        print("Survivors rescued:", people)

    elif choice == "3":
        print("\nAttacking enemy...")
        battery -= 10

        if random.choice([True, False]):
            enemies_defeated += 1
            print("Enemy defeated!")
        else:
            health -= 20
            print("Enemy counterattacked!")

    elif choice == "4":
        if battery >= 10:
            health = min(100, health + 30)
            battery -= 10
            print("Robot repaired!")
        else:
            print("Not enough battery!")

    elif choice == "5":
        print("\nBattery:", battery, "%")
        print("Health:", health, "%")
        print("Survivors:", rescued)
        print("Enemies defeated:", enemies_defeated)

    elif choice == "6":
        print("\nMission abandoned!")
        break

    else:
        print("Invalid command!")

    print("\nBattery:", battery, "%")
    print("Health:", health, "%")

    if battery <= 20:
        print("LOW BATTERY WARNING!")

    if health <= 20:
        print("CRITICAL HEALTH WARNING!")

if rescued >= 10:
    print("\n🏆 MISSION SUCCESS!")
elif health <= 0:
    print("\n💀 ROBOT DESTROYED!")
elif battery <= 0:
    print("\n🔋 ROBOT SHUTDOWN!")

print("\n========== FINAL REPORT ==========")
print("Commander:", player)
print("Survivors rescued:", rescued)
print("Enemies defeated:", enemies_defeated)
print("Final battery:", battery)
print("Final health:", health)
