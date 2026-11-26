import random

print("=" * 45)
print("       ROBOT APOCALYPSE")
print("         BOSS BATTLE")
print("=" * 45)

player = input("\nEnter commander name: ")

battery = 100
health = 100
rescued = 0
enemies_defeated = 0
boss_health = 150

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
    print("5. Fight BOSS")
    print("6. System Status")
    print("7. Exit Mission")

    choice = input("\nEnter command: ")

    if choice == "1":
        for key, location in locations.items():
            print(key + ".", location)

        zone = input("Choose location: ")

        if zone in locations:
            print("Exploring:", locations[zone])
            battery -= 10

            event = random.choice(["enemy", "safe", "survivor"])

            if event == "enemy":
                print("Enemy detected!")
                health -= 15

            elif event == "safe":
                print("Area secured!")

            else:
                print("Survivors found!")
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

        if boss_health <= 0:
            print("Boss is already defeated!")

        elif battery < 15:
            print("Not enough battery for boss battle!")

        else:
            print("\nWARNING! FINAL BOSS ACTIVATED!")
            print("BOSS HEALTH:", boss_health)

            while boss_health > 0 and health > 0 and battery >= 15:

                print("\n1. POWER ATTACK")
                print("2. DEFEND")
                print("3. ESCAPE")

                move = input("Choose your move: ")

                if move == "1":
                    damage = random.randint(20, 40)
                    boss_health = max(0, boss_health - damage)
                    battery -= 15

                    print("You dealt", damage, "damage!")

                elif move == "2":
                    damage = random.randint(5, 15)
                    health -= damage
                    battery -= 5

                    print("You defended the attack!")
                    print("Damage received:", damage)

                elif move == "3":
                    print("You escaped the battle!")
                    break

                else:
                    print("Invalid move!")
                    continue

                if boss_health > 0 and health > 0:
                    boss_damage = random.randint(10, 25)
                    health -= boss_damage

                    print("Boss attacked!")
                    print("Damage received:", boss_damage)

                print("Your health:", health)
                print("Boss health:", boss_health)
                print("Battery:", battery)

            if boss_health <= 0:
                print("\n🏆 FINAL BOSS DEFEATED!")
                enemies_defeated += 1

    elif choice == "6":
        print("\nCommander:", player)
        print("Battery:", battery)
        print("Health:", health)
        print("Survivors:", rescued)
        print("Enemies defeated:", enemies_defeated)
        print("Boss health:", boss_health)

    elif choice == "7":
        print("Mission abandoned!")
        break

    else:
        print("Invalid command!")

    if battery <= 20 and battery > 0:
        print("LOW BATTERY WARNING!")

    if health <= 20 and health > 0:
        print("CRITICAL HEALTH WARNING!")

if rescued >= 10:
    print("\n🏆 CITY RESCUE SUCCESSFUL!")

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
print("Boss remaining health:", boss_health)
