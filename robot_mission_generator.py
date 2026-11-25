import random

missions = [
    "Rescue 10 survivors from the destroyed city.",
    "Destroy the Alien Commander.",
    "Collect 20 Energy Cells.",
    "Protect the underground shelter.",
    "Repair the damaged communication tower.",
    "Defeat 5 enemy robots.",
    "Find the secret military laboratory.",
    "Recover the stolen power core."
]

difficulties = ["EASY", "MEDIUM", "HARD", "EXTREME"]

rewards = [100, 200, 350, 500, 1000]

print("=" * 45)
print("       APOCALYPSE MISSION GENERATOR")
print("=" * 45)

while True:
    print("\n1. Generate New Mission")
    print("2. View Mission Rules")
    print("0. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        mission = random.choice(missions)
        difficulty = random.choice(difficulties)
        reward = random.choice(rewards)

        print("\n***** NEW MISSION *****")
        print("MISSION:", mission)
        print("DIFFICULTY:", difficulty)
        print("REWARD:", reward, "COINS")
        print("STATUS: WAITING FOR COMMANDER")

    elif choice == "2":
        print("\nMISSION RULES")
        print("1. Complete the assigned objective.")
        print("2. Survive enemy attacks.")
        print("3. Collect your mission reward.")
        print("4. Become the ultimate commander.")

    elif choice == "0":
        print("\nMission Generator Offline.")
        break

    else:
        print("Invalid Command!")
