import random

number_to_guess = random.randint(1,100)
correct_guess = False
attempts = 0

print("Lets play a number guessing game.\nI'm thinking of a number between 1 - 100")

while not correct_guess:

    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number_to_guess:
            correct_guess = True
            print("You Got it!")
            print(f"It took {attempts} attempts!")
        elif guess < number_to_guess:
            print("Too low.")
        else:
            print("Too high.")
    except ValueError:
        print("Please enter a valid number.")