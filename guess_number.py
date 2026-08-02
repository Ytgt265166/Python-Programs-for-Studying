import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
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