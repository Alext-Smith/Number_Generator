import random

while True:
    secret_number = random.randint(1, 10)
    attempts = 0
    previous_guesses = []

    while True:
        try:
            guess= int(input("Guess a number between 1 and 10: "))
            if guess <1 or guess > 10:
               print("The number must be between 1 and 10")
               continue

            elif guess in previous_guesses:
                print("You have already guessed this number ")
                continue

            else:
                attempts += 1
                previous_guesses.append(guess)
                if guess == secret_number:
                   print(f"🎉 Correct! You guessed it in {attempts} attempts!")
                   break
                elif guess < secret_number:
                   print("Too low! Try again.")
                else:
                   print("Too high! Try again.")

                print(f"You have {3 - attempts} guesses remaining")

            if attempts == 3:
               print(f"You were unable to guess the secret number. The number was {secret_number}")
               break

        except ValueError:
            print("Please input a value between 1 and 10 in the numerical format.")

    again = input("\nWould you like to have another go? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break
