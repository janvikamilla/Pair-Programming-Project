import random
import time

print("=" * 45)
print("       ☢️ FINAL APOCALYPSE")
print("         END OF THE WORLD")
print("=" * 45)

commander = input("\nEnter commander name: ")

health = 100
battery = 100
survivors = 0
city_power = 100

print("\nWARNING! NUCLEAR MELTDOWN DETECTED!")
print("Humanity is depending on you!")
print("\nYou have 60 seconds to save the city.")

time.sleep(2)

for minute in range(1, 7):

    print("\n========== EMERGENCY ==========")
    print("Time remaining:", 60 - (minute - 1) * 10, "seconds")

    print("\n1. Rescue survivors")
    print("2. Stop nuclear reactor")
    print("3. Activate city shield")
    print("4. Recharge robot")
    print("5. Check system status")

    choice = input("\nChoose your action: ")

    if choice == "1":
        people = random.randint(2, 5)
        survivors += people
        battery -= 10
        print("Rescued", people, "survivors!")

    elif choice == "2":
        if random.choice([True, False]):
            city_power += 20
            print("Reactor successfully controlled!")
        else:
            health -= 20
            print("Reactor explosion! Robot damaged!")

        battery -= 15

    elif choice == "3":
        city_power += 15
        battery -= 20
        print("City shield activated!")

    elif choice == "4":
        battery = min(100, battery + 30)
        print("Battery restored!")

    elif choice == "5":
        print("Health:", health)
        print("Battery:", battery)
        print("Survivors:", survivors)
        print("City power:", city_power)

    else:
        print("Invalid action!")
        health -= 10

    if battery <= 0:
        print("\nROBOT POWER LOST!")
        break

    if health <= 0:
        print("\nROBOT DESTROYED!")
        break

    disaster = random.choice([
        "Meteor shower approaching!",
        "Alien attack detected!",
        "Earthquake detected!",
        "No new disaster!"
    ])

    print("\nDISASTER UPDATE:", disaster)

    if disaster != "No new disaster!":
        health -= 5

    time.sleep(1)

print("\n" + "=" * 45)
print("          FINAL APOCALYPSE REPORT")
print("=" * 45)

print("Commander:", commander)
print("Survivors saved:", survivors)
print("Robot health:", health)
print("Robot battery:", battery)
print("City power:", city_power)

if survivors >= 15 and city_power >= 100:
    print("\n🏆 LEGENDARY ENDING!")
    print("You saved humanity completely!")

elif survivors >= 8:
    print("\n⭐ HUMANITY SURVIVED!")
    print("The city has a second chance.")

elif survivors >= 1:
    print("\n⚠️ PARTIAL SURVIVAL!")
    print("Some survivors escaped.")

else:
    print("\n☠️ APOCALYPSE ENDING!")
    print("The city has fallen.")

print("\nMISSION COMPLETE.")
