import json
import os

print("=" * 45)
print("       PLAYER ACHIEVEMENT SYSTEM")
print("=" * 45)

filename = "player_profile.json"

if os.path.exists(filename):
    with open(filename, "r") as file:
        profile = json.load(file)
else:
    name = input("\nEnter commander name: ")

    profile = {
        "name": name,
        "xp": 0,
        "missions": 0,
        "survivors": 0,
        "bosses": 0,
        "badges": []
    }

print("\nWelcome back,", profile["name"])

print("\n1. Complete a mission")
print("2. Rescue survivors")
print("3. Defeat a boss")
print("4. View player profile")

choice = input("\nChoose activity: ")

if choice == "1":
    profile["missions"] += 1
    profile["xp"] += 100
    print("Mission completed! +100 XP")

elif choice == "2":
    profile["survivors"] += 5
    profile["xp"] += 150
    print("5 survivors rescued! +150 XP")

elif choice == "3":
    profile["bosses"] += 1
    profile["xp"] += 300
    print("Boss defeated! +300 XP")

elif choice == "4":
    print("\nPLAYER PROFILE")
    print("Commander:", profile["name"])
    print("XP:", profile["xp"])

else:
    print("Invalid activity!")

# Achievement system

achievements = {
    "FIRST MISSION": profile["missions"] >= 1,
    "LIFE SAVER": profile["survivors"] >= 5,
    "BOSS SLAYER": profile["bosses"] >= 1,
    "LEGENDARY COMMANDER": profile["xp"] >= 1000
}

for badge, unlocked in achievements.items():

    if unlocked and badge not in profile["badges"]:
        profile["badges"].append(badge)
        print("\n🏆 NEW BADGE UNLOCKED:", badge)

level = (profile["xp"] // 500) + 1

print("\n========== PLAYER STATUS ==========")
print("Commander:", profile["name"])
print("XP:", profile["xp"])
print("Level:", level)
print("Missions:", profile["missions"])
print("Survivors:", profile["survivors"])
print("Bosses defeated:", profile["bosses"])

print("\nUNLOCKED BADGES:")

for badge in profile["badges"]:
    print("🏆", badge)

with open(filename, "w") as file:
    json.dump(profile, file, indent=4)

print("\nPLAYER DATA SAVED SUCCESSFULLY!")
