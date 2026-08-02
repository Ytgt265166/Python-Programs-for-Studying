import random

def guess_number():
    range = 300
    number_to_guess = random.randint(1, range)
    attempts = 0
    guessed = False

    print("Welcome to the Guess the Number Game!")
    print(f"I have selected a number between 1 and {range}. Can you guess it?")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > range:
                print(f"Please enter a number between 1 and {range}.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

#guess_number()            
if __name__ == "__main__":
    guess_number()