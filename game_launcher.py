import os
import sys
import subprocess

def show_menu():
    print("\n" + "=" * 40)
    print("       ROBOT APOCALYPSE")
    print("        MAIN CONTROL HUB")
    print("=" * 40)

    print("1. Main Survival Mission")
    print("2. Disaster Alert System")
    print("3. Robot Army")
    print("4. Alien Invasion")
    print("5. Black Market")
    print("6. Hacking Terminal")
    print("7. Final Apocalypse")
    print("8. Player Achievements")
    print("9. Robot Battle Arena")
    print("10. Robot Inventory")
    print("0. Exit Game")

    print("=" * 40)


games = {
    "1": "robot_apocalypse.py",
    "2": "disaster_events.py",
    "3": "robot_army.py",
    "4": "alien_invasion.py",
    "5": "black_market.py",
    "6": "hacking_terminal.py",
    "7": "final_apocalypse.py",
    "8": "player_achievements.py",
    "9": "robot_battle_arena.py",
    "10": "robot_inventory.py"
}

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "0":
        print("Goodbye, Commander!")
        break

    elif choice in games:
        selected_game = games[choice]

        if os.path.exists(selected_game):
            subprocess.run([sys.executable, selected_game])
        else:
            print("Game file not found!")

    else:
        print("Invalid choice!")
