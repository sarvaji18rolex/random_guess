import random

def number_guess_game():
    print("🎯 Welcome to the Number Guessing Game!") 
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number 
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (or 'q' to quit): ")

        if guess.lower() == 'q':
            print("👋 Thanks for playing! Goodbye.")
            break

        if not guess.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("🔼 Too low! Try again.")
        elif guess > secret_number:
            print("🔽 Too high! Try again.")
        else:
            print(f"✅ Correct! The number was {secret_number}.")
            print(f"🎉 You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guess_game()



