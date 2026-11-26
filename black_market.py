import random

print("=" * 45)
print("       ☠️ UNDERGROUND BLACK MARKET")
print("             WEAPON SHOP")
print("=" * 45)

coins = 500
inventory = []

weapons = {
    "1": {"name": "Laser Gun", "price": 100, "power": 30},
    "2": {"name": "Plasma Cannon", "price": 200, "power": 60},
    "3": {"name": "Thunder Blade", "price": 300, "power": 90},
    "4": {"name": "Quantum Launcher", "price": 450, "power": 150}
}

while True:

    print("\n========== BLACK MARKET ==========")
    print("Available Coins:", coins)
    print("\n1. View Weapons")
    print("2. Buy Weapon")
    print("3. Earn Coins")
    print("4. View Inventory")
    print("5. Exit Shop")

    choice = input("\nEnter choice: ")

    if choice == "1":

        print("\nAVAILABLE WEAPONS")

        for key, weapon in weapons.items():
            print(key, weapon["name"])
            print("Price:", weapon["price"])
            print("Attack Power:", weapon["power"])
            print("----------------------")

    elif choice == "2":

        for key, weapon in weapons.items():
            print(key, weapon["name"], "-", weapon["price"], "coins")

        purchase = input("\nSelect weapon: ")

        if purchase in weapons:

            weapon = weapons[purchase]

            if weapon["name"] in inventory:
                print("You already own this weapon!")

            elif coins >= weapon["price"]:
                coins -= weapon["price"]
                inventory.append(weapon["name"])

                print("\nPURCHASE SUCCESSFUL!")
                print("Weapon acquired:", weapon["name"])

            else:
                print("Not enough coins!")

        else:
            print("Invalid weapon!")

    elif choice == "3":

        reward = random.randint(50, 150)
        coins += reward

        print("\nMission completed!")
        print("You earned", reward, "coins!")

    elif choice == "4":

        print("\nYOUR WEAPON INVENTORY")

        if inventory:
            for weapon in inventory:
                print("-", weapon)
        else:
            print("Your inventory is empty!")

    elif choice == "5":
        print("\nLeaving Black Market...")
        break

    else:
        print("Invalid choice!")

print("\nFINAL COINS:", coins)
print("Thanks for visiting the Black Market!")
