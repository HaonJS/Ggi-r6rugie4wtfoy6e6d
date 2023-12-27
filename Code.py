import random
import os

def facebook_code_cracker():
    # Prompt the user to enter the phone number or email address
    user_input = input("Enter the phone number or email address: ")

    # Generate a random code between 1000 and 100000
    code = random.randint(1000, 100000)

    # Keep guessing until the correct code is found
    while True:
        # Prompt the user to enter their guess
        guess = int(input("Enter your guess: "))

        # Check if the guess is too low
        if guess < code:
            print("Too low! Try again.")

        # Check if the guess is too high
        elif guess > code:
            print("Too high! Try again.")

        # The guess is correct
        else:
            print("Congratulations! You cracked the code!")
            break

    # Display the correct code
    print("The correct code is:", code)

# Call the function to start the Facebook Code Cracker
facebook_code_cracker()

def print_welcome_message():
    welcome_message = """
╭───────────────  [  WELCOME ] ────────────────╮
│                                             │
│     THIS IS CREATED BY YENZY                │
│         [ GITHUB : YENZYJS ]                │
│                                             │
╰─────────────────────────────────────────────╯
"""
    print(welcome_message)

def main():
    print_welcome_message()
    Facebook_Code_Cracker()  # Correct function call
    # Add your tool's main functionality here

if __name__ == "__main__":
    main()
