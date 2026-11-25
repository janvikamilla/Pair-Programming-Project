import random

player_health = 100
enemy_health = 100

print("=" * 40)
print("       AI ENEMY INTELLIGENCE")
print("=" * 40)

while player_health > 0 and enemy_health > 0:

    print("\nYOUR HEALTH:", player_health)
    print("ENEMY HEALTH:", enemy_health)

    print("\n1. Attack")
    print("2. Defend")
    print("3. Repair")

    choice = input("\nChoose your action: ")

    if choice == "1":
        damage = random.randint(15, 30)
        enemy_health -= damage
        print("\nYou attacked the enemy!")
        print("Damage:", damage)

    elif choice == "2":
        print("\nYou entered defensive mode!")

    elif choice == "3":
        player_health = min(100, player_health + 20)
        print("\nRobot repaired!")

    else:
        print("Invalid action!")
        continue

    if enemy_health <= 0:
        break

    print("\nAI ANALYSING YOUR MOVEMENT...")

    if player_health < 30:
        ai_action = "ATTACK"
    elif enemy_health < 30:
        ai_action = random.choice(["ATTACK", "DEFEND"])
    else:
        ai_action = random.choice(["ATTACK", "DEFEND", "SPECIAL"])

    if ai_action == "ATTACK":
        damage = random.randint(15, 25)
        player_health -= damage
        print("AI launched an attack!")
        print("Damage received:", damage)

    elif ai_action == "DEFEND":
        print("AI activated defensive shield!")

    else:
        damage = random.randint(25, 35)
        player_health -= damage
        print("AI USED SPECIAL ATTACK!")
        print("Damage received:", damage)

print("\n" + "=" * 40)

if player_health > 0:
    print("VICTORY! YOU DEFEATED THE AI!")
else:
    print("DEFEAT! AI DESTROYED YOUR ROBOT.")

print("=" * 40)
