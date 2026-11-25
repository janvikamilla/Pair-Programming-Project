import random

print("=" * 45)
print("       ROBOT APOCALYPSE")
print("          ROBOT ARMY")
print("=" * 45)

robots = {
    "1": {
        "name": "WARRIOR BOT",
        "power": 90,
        "defence": 40,
        "speed": 50
    },
    "2": {
        "name": "RESCUE BOT",
        "power": 40,
        "defence": 60,
        "speed": 70
    },
    "3": {
        "name": "SHIELD BOT",
        "power": 30,
        "defence": 100,
        "speed": 30
    },
    "4": {
        "name": "SPEED BOT",
        "power": 60,
        "defence": 40,
        "speed": 100
    },
    "5": {
        "name": "ENERGY BOT",
        "power": 50,
        "defence": 60,
        "speed": 60
    }
}

print("\nYOUR ROBOT COLLECTION")

for key, bot in robots.items():
    print(key + ".", bot["name"])

choice = input("\nChoose your robot: ")

if choice in robots:

    selected = robots[choice]

    print("\nROBOT ACTIVATED!")
    print("Name:", selected["name"])
    print("Power:", selected["power"])
    print("Defence:", selected["defence"])
    print("Speed:", selected["speed"])

    print("\nUPGRADE SYSTEM")
    print("1. Upgrade Power")
    print("2. Upgrade Defence")
    print("3. Upgrade Speed")

    upgrade = input("\nChoose upgrade: ")

    if upgrade == "1":
        selected["power"] += 20

    elif upgrade == "2":
        selected["defence"] += 20

    elif upgrade == "3":
        selected["speed"] += 20

    else:
        print("Invalid upgrade!")

    print("\nUPGRADE COMPLETE!")
    print("New Robot Statistics:")

    for stat, value in selected.items():
        print(stat, ":", value)

else:
    print("Invalid robot selection!")

print("\n🤖 ROBOT ARMY READY FOR BATTLE!")
