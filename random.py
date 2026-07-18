import random as r
a = r.randint(2,8)
print(a)
print(r.random())
print(r.choice('computer'))



# task 1
# Write a program to generate a random integer and match it with the input given by the user?

import random as r
guess = r.randint(1,6)
print("Try and guess the correct value to win")
guess_input = int(input("Enter a guessed value: "))
if guess_input == guess:
    print("You win")
else:
    print("Guess again")
    

# task 2
# Create a program to play rock, paper, and scissors. Use a random module to select 
# from the given options Check whether the random guess matches the user’s answer

import random as r
 
choice = input("Do u want to play rock, paper, scissors, game, (yes/no): ")
if choice == "yes":
    uchoice = input("Enter either, rock(r), paper(p) or scissors(S): ")
    cchoice = r.randint(1,3)
    if cchoice == 1:
        cchoice = "r"
    elif cchoice == 2:
        cchoice = "p"
    else:
        cchoice = "s"
    print("cchoice =", cchoice)

    if uchoice == "r":
        if cchoice == "r":
            print('its a tie')
        elif cchoice == "p":
            print('computer wins')
        else:
            print('user wins')

    elif uchoice == "p":
        if cchoice == "r":
            print('user wins')
        elif cchoice == "p":
            print('its a tie')
        else:
            print('computer wins')

    elif uchoice == "s":
        if cchoice == "r":
            print('computer wins')
        elif cchoice == "p":
            print('user wins')
        else:
            print('its a tie')

else:
    exit()

