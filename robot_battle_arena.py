import random
import time

print("=" * 40)
print("       ROBOT BATTLE ARENA")
print("=" * 40)

player_health = 100
enemy_health = 100
energy = 50
round_number = 1

print("\nYour robot is ready for battle!")
print("Enemy robot detected!")

while player_health > 0 and enemy_health > 0:

    print("\n---------- ROUND", round_number, "----------")
    print("Your Health:", player_health)
    print("Enemy Health:", enemy_health)
    print("Energy:", energy)

    print("\n1. Normal Attack")
    print("2. Heavy Attack")
    print("3. Special Power")
    print("4. Repair Robot")

    choice = input("\nChoose your move: ")

    if choice == "1":
        damage = random.randint(10, 20)
        enemy_health -= damage
        print("\nYou dealt", damage, "damage!")

    elif choice == "2":
        if energy >= 15:
            damage = random.randint(25, 35)
            enemy_health -= damage
            energy -= 15
            print("\nHEAVY ATTACK!")
            print("Damage:", damage)
        else:
            print("Not enough energy!")

    elif choice == "3":
        if energy >= 30:
            damage = random.randint(40, 50)
            enemy_health -= damage
            energy -= 30
            print("\nSPECIAL POWER ACTIVATED!")
            print("MEGA DAMAGE:", damage)
        else:
            print("Not enough energy!")

    elif choice == "4":
        healing = random.randint(15, 25)
        player_health += healing
        player_health = min(player_health, 100)
        print("\nRobot repaired!")
        print("Health restored:", healing)

    else:
        print("Invalid move!")
        continue

    if enemy_health <= 0:
        break

    time.sleep(1)

    enemy_damage = random.randint(10, 20)
    player_health -= enemy_damage

    print("\nEnemy attacked!")
    print("You lost", enemy_damage, "health.")

    energy = min(energy + 5, 50)
    round_number += 1

print("\n" + "=" * 40)

if player_health > 0:
    print("🏆 VICTORY! YOU DEFEATED THE ENEMY!")
else:
    print("💀 DEFEAT! YOUR ROBOT WAS DESTROYED.")

print("Battle Rounds:", round_number)
print("=" * 40)
