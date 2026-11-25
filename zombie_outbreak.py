import random

health = 100
score = 0
round_number = 1

zombies = {
    "Walker": 15,
    "Runner": 25,
    "Mutant": 40,
    "Mega Zombie": 60
}

print("=" * 40)
print("       ZOMBIE OUTBREAK")
print("=" * 40)

while health > 0:

    zombie = random.choice(list(zombies.keys()))
    damage = zombies[zombie]

    print("\nROUND:", round_number)
    print("A", zombie, "has appeared!")
    print("Zombie Power:", damage)
    print("Your Health:", health)
    print("Survival Score:", score)

    print("\n1. Attack")
    print("2. Escape")
    print("3. Use Emergency Shield")

    choice = input("\nChoose your action: ")

    if choice == "1":
        attack = random.randint(20, 50)

        print("\nYou attacked the zombie!")
        print("Damage dealt:", attack)

        if attack >= damage:
            print("ZOMBIE DEFEATED!")
            score += 100
        else:
            health -= damage
            print("Zombie attacked you!")
            print("Health lost:", damage)

    elif choice == "2":
        escape = random.choice([True, False])

        if escape:
            print("Successfully escaped!")
            score += 30
        else:
            health -= damage
            print("Escape failed! Zombie attacked!")

    elif choice == "3":
        print("Emergency shield activated!")
        print("You escaped this round safely!")
        score += 20

    else:
        print("Invalid action!")
        continue

    round_number += 1

    if round_number > 10:
        print("\nYOU SURVIVED THE OUTBREAK!")
        break

print("\n" + "=" * 40)
print("       ZOMBIE OUTBREAK RESULTS")
print("=" * 40)
print("Final Health:", max(0, health))
print("Final Score:", score)
print("Rounds Survived:", round_number - 1)
print("MISSION COMPLETE!")
