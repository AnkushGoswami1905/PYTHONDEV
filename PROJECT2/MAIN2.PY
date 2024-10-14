import random

def guessing_game():
    # Generate a random secret number between 1 and 100
    r = 69
    low = 1
    high = 100
    n = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while low <= high:
        n += 1
        g = (low + high) // 2  # Guess the midpoint
        print(f"My guess is: {g}")

        if g > r:
            print("Lower!")
            high = g - 1  # Adjust the upper bound
        elif g < r:
            print("Higher!")
            low = g + 1  # Adjust the lower bound
        else:
            print(f"You have guessed the number {r} correctly in {n} attempts!")
            break

# Call the game function
guessing_game()
