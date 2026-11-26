import random

print("=" * 45)
print("       CYBER WARFARE SYSTEM")
print("          HACKING TERMINAL")
print("=" * 45)

secret_code = random.randint(1000, 9999)
attempts = 5
hacked = False
data_coins = 0

print("\nENEMY DATABASE DETECTED!")
print("Security system activated.")
print("Crack the 4-digit access code.")

while attempts > 0:

    print("\nAttempts remaining:", attempts)

    guess = input("Enter access code: ")

    if not guess.isdigit() or len(guess) != 4:
        print("Enter a valid 4-digit code!")
        continue

    guess = int(guess)

    if guess == secret_code:
        print("\nACCESS GRANTED!")
        hacked = True
        data_coins = 200
        break

    elif guess < secret_code:
        print("Hint: Try a HIGHER code!")

    else:
        print("Hint: Try a LOWER code!")

    attempts -= 1

if hacked:
    print("\nENEMY DATABASE HACKED!")
    print("You earned", data_coins, "data coins!")
else:
    print("\nACCESS DENIED!")
    print("The secret code was:", secret_code)

print("\nHACKING SESSION TERMINATED.")
