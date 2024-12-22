# import module
import random

# create a function
def start_game():
    number_to_guess = random.randint(1, 100)   # create a random number from 0 to 100
    guess = None                                     # user number
    tries = 0                                        # number of attempts

    # create a loop
    while guess != number_to_guess:
        guess = int(input("Guess the number from 1 to 100: "))    # user input
        tries += 1                                          # add more try
        if guess < number_to_guess:                         # output if the number is less
            print("Too little! Try again.")
        elif guess > number_to_guess:                       # output if the number is greater
            print("Too much! Try again.")

    # output with the guessed number and the number of attempts
    print(f"Congratulations! You guessed the number. {number_to_guess} in {tries} tries.")


if __name__ == "__main__":
    start_game()