import random

# Generate a random 4-digit number and convert to string
number = str(random.randint(1,11))
print("Guess the 4-digit number, one digit at a time.")
chances = 4
# Loop over each digit in the number
for i in range(1,chances+1):
    guess = input("Enter a digit: ")

    # Check if input is valid
    if not guess.isdigit() or len(guess) != 1:
        print("Please enter a single digit.")
        continue

    if guess == i:
        print("You guessed a digit right:", i)
    else:
        print("Wrong guess. Try the next digit.")
        print("_")

    chances = chances - 1

print("The number was:", number)
