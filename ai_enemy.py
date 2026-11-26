import random

player_health = 100
enemy_health = 100

print("=" * 40)
print("AI ENEMY INTELLIGENCE")
print("=" * 40)

while player_health > 0 and enemy_health > 0:

    print("\nYOUR HEALTH:", player_health)
    print("ENEMY HEALTH:", enemy_health)

    print("\n1. Attack")
    print("2. Defend")
    print("3. Repair")

    choice = input("Choose your action: ")

    defending = False

    if choice == "1":
        damage = random.randint(15, 30)
        enemy_health -= damage
        print("You attacked!")
        print("Damage:", damage)

    elif choice == "2":
        defending = True
        print("Defensive mode activated!")

    elif choice == "3":
        player_health = min(100, player_health + 20)
        print("Robot repaired!")

    else:
        print("Invalid choice!")
        continue

    if enemy_health <= 0:
        break

    print("\nAI ANALYSING YOUR MOVEMENT...")

    if player_health < 30:
        ai_action = "ATTACK"
    else:
        ai_action = random.choice(
            ["ATTACK", "DEFEND", "SPECIAL"]
        )

    if ai_action == "ATTACK":
        damage = random.randint(15, 25)

    elif ai_action == "SPECIAL":
        damage = random.randint(25, 35)

    else:
        damage = 0
        print("AI activated its shield!")

    if defending:
        damage = damage // 2

    player_health -= damage

    print("AI action:", ai_action)
    print("Damage received:", damage)

print("\n========== BATTLE RESULT ==========")

if player_health > 0:
    print("VICTORY! YOU DEFEATED THE AI!")
else:
    print("DEFEAT! AI DESTROYED YOUR ROBOT.")

print("Final Player Health:", max(0, player_health))
print("Final Enemy Health:", max(0, enemy_health))
