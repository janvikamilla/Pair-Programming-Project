print("=" * 40)
print("       ROBOT CUSTOMIZATION GARAGE")
print("=" * 40)

robot_name = "APOCALYPSE-X"
armor = 50
attack = 40
speed = 30
coins = 200

while True:
    print("\n===== ROBOT GARAGE =====")
    print("Coins:", coins)
    print("1. Change Robot Name")
    print("2. Upgrade Armor - 50 coins")
    print("3. Upgrade Attack - 70 coins")
    print("4. Upgrade Speed - 60 coins")
    print("5. View Robot Stats")
    print("0. Exit Garage")

    choice = input("\nChoose an option: ")

    if choice == "1":
        robot_name = input("Enter new robot name: ")
        print("Robot renamed successfully!")

    elif choice == "2":
        if coins >= 50:
            armor += 10
            coins -= 50
            print("Armor upgraded!")
        else:
            print("Not enough coins!")

    elif choice == "3":
        if coins >= 70:
            attack += 10
            coins -= 70
            print("Attack upgraded!")
        else:
            print("Not enough coins!")

    elif choice == "4":
        if coins >= 60:
            speed += 10
            coins -= 60
            print("Speed upgraded!")
        else:
            print("Not enough coins!")

    elif choice == "5":
        print("\n===== ROBOT SPECIFICATIONS =====")
        print("Name:", robot_name)
        print("Armor:", armor)
        print("Attack:", attack)
        print("Speed:", speed)
        print("Coins:", coins)

    elif choice == "0":
        print("Leaving Robot Garage...")
        break

    else:
        print("Invalid choice!")
