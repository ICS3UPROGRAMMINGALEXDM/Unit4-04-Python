#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/30/2022
# Description: This program generates a random number that
# the user must guess correctly to win the game
# now with funny colors

import math
import random
import sys

import colorama
from colorama import Back, Fore, Style


def main():
    # booleans for loops
    restart_loop = True
    guess_loop = True

    # loop to run the game again if user responds yes
    while restart_loop:
        # Creating the random number
        r_num = random.randint(1, 15)
        print(
            Fore.WHITE
            + "I just generated a random number "
            + "between 1-15. Can you Guess it correctly?"
        )
        print(r_num)

        # Loop allows user to keep guessing until they get it right
        while guess_loop:
            u_num = input(Fore.WHITE + "Input your number below:\n")

            try:
                u_num = int(u_num)

                # Comparing user number with random number
                if u_num == r_num:
                    print(
                        Fore.GREEN
                        + "Congratulations,"
                        + " you guessed the number correctly!!"
                    )
                    answer = (
                        input(Fore.WHITE + "Would you like to play again? (y/n):")
                        .strip()
                        .lower()
                    )

                    # what to do with user answer
                    if answer == "y":
                        print("Okay")
                        break
                    else:
                        print("Okay")
                        # Ends program
                        restart_loop = False
                        guess_loop = False
                else:
                    print(Fore.RED + "Uh oh, wrong answer. Guess again!")

            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Invalid input, try again.")


if __name__ == "__main__":
    main()
