import random

inventory = {
    "Health Kit": 2,
    "Energy Cell": 3,
    "Laser Gun": 1,
    "Shield": 1
}

capacity = 10

def show_inventory():
    print("\n===== ROBOT INVENTORY =====")
    total = 0

    for item, quantity in inventory.items():
        print(item, ":", quantity)
        total += quantity

    print("Items used:", total, "/", capacity)


def collect_item():
    items = ["Health Kit", "Energy Cell", "Laser Gun", "Shield"]
    item = random.choice(items)

    total = sum(inventory.values())

    if total < capacity:
        inventory[item] += 1
        print("\nCollected:", item)
    else:
        print("\nInventory Full!")


def use_item():
    print("\n1. Health Kit")
    print("2. Energy Cell")

    choice = input("Choose item: ")

    if choice == "1":
        if inventory["Health Kit"] > 0:
            inventory["Health Kit"] -= 1
            print("Health restored!")
        else:
            print("No Health Kits available!")

    elif choice == "2":
        if inventory["Energy Cell"] > 0:
            inventory["Energy Cell"] -= 1
            print("Energy restored!")
        else:
            print("No Energy Cells available!")

    else:
        print("Invalid choice!")


while True:
    print("\n===== ROBOT INVENTORY SYSTEM =====")
    print("1. View Inventory")
    print("2. Collect Random Item")
    print("3. Use Item")
    print("4. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        show_inventory()

    elif choice == "2":
        collect_item()

    elif choice == "3":
        use_item()

    elif choice == "4":
        print("Inventory System Closed!")
        break

    else:
        print("Invalid Option!")
