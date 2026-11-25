import os
import sys
import subprocess

def show_menu():
    print("\n" + "=" * 45)
    print("          ROBOT APOCALYPSE")
    print("           MAIN CONTROL HUB")
    print("=" * 45)

    games = {
        "1": ("Main Survival Mission", "robot_apocalypse.py"),
        "2": ("Disaster Alert System", "disaster_events.py"),
        "3": ("Robot Army", "robot_army.py"),
        "4": ("Alien Invasion", "alien_invasion.py"),
        "5": ("Black Market", "black_market.py"),
        "6": ("Hacking Terminal", "hacking_terminal.py"),
        "7": ("Final Apocalypse", "final_apocalypse.py"),
        "8": ("Player Achievements", "player_achievements.py"),
        "9": ("Robot Battle Arena", "robot_battle_arena.py"),
        "10": ("Robot Inventory", "robot_inventory.py"),
        "11": ("Robot Customization", "robot_customization.py"),
        "12": ("Mission Generator", "robot_mission_generator.py")
    }

    for number, (name, filename) in games.items():
        print(number + ". " + name)

    print("0. Exit Game")
    print("=" * 45)

    return games


while True:
    games = show_menu()
    choice = input("\nEnter your choice: ")

    if choice == "0":
        print("System shutting down...")
        break

    elif choice in games:
        selected_game = games[choice][1]

        if os.path.exists(selected_game):
            subprocess.run([sys.executable, selected_game])
        else:
            print("ERROR: Game file not found!")

    else:
        print("Invalid choice!")
