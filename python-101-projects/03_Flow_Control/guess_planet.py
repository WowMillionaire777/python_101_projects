"""
Friends from Earth 🌏 want to know were is Louis, so Louis decides to
write a program that will make his friends guess the name of planet.
"""

correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"

# ----------------------------------------------------
# Alternative 1
# ----------------------------------------------------


# while correct_guess is not True:
#     # Prompt user to enter a guess and assign it to 'guess' variable
#     guess = input("Louis Says: Can you guess my planet? >>> ")
#     if guess.lower() == planet.lower():
#         print("Right guess!! Louis is from Zortan.")
#         print("Thanks for playing!!")
#         # Set the 'correct_guess' to 'True and break from 'while' loop
#         correct_guess = True
#     else:
#         # Display a message for wrong guess
#         print("Louis Says: Sorry wrong choice, try again!!")
#         print("-------------------------------------------")
#         print("")

# ----------------------------------------------------
# Alternative 2
# ----------------------------------------------------

while True:
    # Prompt user to enter a guess and assign it to 'guess' variable
    guess = input("Louis Says: Can you guess my planet? >>> ")
    if guess.lower() == planet.lower():
        print("Right guess!! Louis is from Zortan.")
        print("Thanks for playing!!")
        # Set the 'correct_guess' to 'True and break from 'while' loop
        break
    else:
        # Display a message for wrong guess
        print("Louis Says: Sorry wrong choice, try again!!")
        print("-------------------------------------------")
        print("")
