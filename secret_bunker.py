import random

survivors = 10
food = 100
water = 100
electricity = 100
security = 80
day = 1

print("=" * 45)
print("       SECRET UNDERGROUND BUNKER")
print("=" * 45)

while survivors > 0:

    print("\n========== DAY", day, "==========")
    print("Survivors:", survivors)
    print("Food:", food)
    print("Water:", water)
    print("Electricity:", electricity)
    print("Security:", security)

    print("\n1. Collect Food")
    print("2. Collect Water")
    print("3. Repair Electricity")
    print("4. Improve Security")
    print("5. Welcome New Survivors")
    print("6. End Day")

    choice = input("\nChoose action: ")

    if choice == "1":
        food += 30
        print("Food supplies increased!")

    elif choice == "2":
        water += 30
        print("Water supplies increased!")

    elif choice == "3":
        electricity = min(100, electricity + 25)
        print("Electricity repaired!")

    elif choice == "4":
        security = min(100, security + 20)
        print("Bunker security improved!")

    elif choice == "5":
        new_people = random.randint(1, 5)
        survivors += new_people
        print(new_people, "new survivors joined!")

    elif choice == "6":
        food -= survivors * 2
        water -= survivors * 2
        electricity -= 5

        if food < 0:
            survivors -= 2
            food = 0
            print("Food shortage! Survivors are leaving.")

        if water < 0:
            survivors -= 2
            water = 0
            print("Water shortage! Survivors are leaving.")

        if electricity < 0:
            electricity = 0
            print("POWER FAILURE!")

        if random.randint(1, 100) <= 25:
            print("\nWARNING! ZOMBIES ATTACKING THE BUNKER!")

            if security >= 50:
                security -= 15
                print("Bunker defended successfully!")
            else:
                survivors -= 3
                print("Zombies entered! Survivors lost!")

        day += 1

    else:
        print("Invalid choice!")

    survivors = max(0, survivors)

    if food > 200:
        food = 200

    if water > 200:
        water = 200

    if survivors <= 0:
        print("\nALL SURVIVORS LOST!")
        print("BUNKER COLLAPSED!")
        break

print("\nBunker Simulation Ended.")
print("Days Survived:", day - 1)
print("Final Survivors:", survivors)
