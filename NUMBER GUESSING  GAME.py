import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("Please choose a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too Low! Try again.")
    elif guess > secret_number:
        print("📈 Too High! Try again.")
    else:
        print("🎉 Congratulations!")
        print(f"You guessed the number {secret_number} correctly.")
        print(f"It took you {attempts} attempts.")
        break