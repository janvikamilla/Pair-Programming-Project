import random

print("=" * 45)
print("       👽 ALIEN INVASION")
print("        SECRET MISSIONS")
print("=" * 45)

score = 0
completed = 0

missions = [
    "Destroy the alien spaceship",
    "Rescue trapped scientists",
    "Protect the power station",
    "Find the alien control chip",
    "Defeat the alien commander"
]

print("\nCLASSIFIED MISSION LIST")

for i, mission in enumerate(missions, 1):
    print(i, ".", mission)

print("\nYour secret mission begins!")

while missions:

    print("\nAVAILABLE MISSIONS:")

    for i, mission in enumerate(missions, 1):
        print(i, ".", mission)

    choice = input("\nSelect mission number (0 to exit): ")

    if choice == "0":
        break

    if not choice.isdigit():
        print("Invalid input!")
        continue

    choice = int(choice)

    if choice < 1 or choice > len(missions):
        print("Mission not available!")
        continue

    mission = missions.pop(choice - 1)

    print("\nMISSION:", mission)
    print("Alien forces detected!")

    result = random.choice(["success", "failure"])

    if result == "success":
        reward = random.randint(50, 200)
        score += reward
        completed += 1

        print("MISSION SUCCESSFUL!")
        print("Reward:", reward, "points")

    else:
        print("MISSION FAILED!")
        print("Alien forces escaped!")

print("\n========== FINAL REPORT ==========")
print("Missions completed:", completed)
print("Total score:", score)

if completed == 5:
    print("🏆 LEGENDARY COMMANDER!")
elif completed >= 3:
    print("⭐ ELITE COMMANDER!")
else:
    print("Keep training, Commander!")

print("\nALIEN MISSION SYSTEM OFFLINE.")
