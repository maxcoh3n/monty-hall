import random

from random import choice


def print_doors(selection=[], goatDoors=[], prizeDoor=None):

    ans = ["?", "?", "?"]

    selection_list = ["", "", ""]

    if prizeDoor != None:
        ans[prizeDoor] = "$"

        for i in range(len(ans)):
            if i != prizeDoor:
                ans[i] = "X"

    else:
        for door in goatDoors:
            ans[door] = "X"

    print("|{}| |{}| |{}|\n 0   1   2".format(ans[0], ans[1], ans[2]))

    if len(selection) > 0:
        selection_list[selection[0]] = "^"

        print(
            "{}    {}     {}".format(
                selection_list[0], selection_list[1], selection_list[2]
            )
        )


def door_selection():

    while True:
        selection = input("Select door 0,1, or 2\n")

        try:
            selection = int(selection)

        except:
            print("invalid selection.")

            continue

        if selection < 0 or selection > 2:
            continue

        else:
            return selection


def monty_hall_helper_manual(evil=False, blind=True):

    wins, trials = 0, 0

    trueWins, trueTrials = 0, 0

    while True:
        doors = [0, 0, 0]

        prize = random.randint(0, 2)

        doors[prize] = 1

        print_doors()

        selection = door_selection()

        if not evil or prize == selection:
            if not blind:
                revealedDoor = choice(
                    [i for i in range(0, 3) if i not in [selection, prize]]
                )

            else:
                revealedDoor = choice([i for i in range(0, 3) if i != selection])

            if revealedDoor == prize:
                print(
                    "Oops! The host revealed that the prize is behind door {}".format(
                        revealedDoor
                    )
                )

            else:
                print_doors(selection=[selection])

                print(
                    "Surprise! The host revealed that the prize is not behind door {}".format(
                        revealedDoor
                    )
                )

                print_doors(selection=[selection], goatDoors=[revealedDoor])

                trueTrials += 1

                if revealedDoor + selection == 1:
                    remaining = 2

                elif revealedDoor + selection == 2:
                    remaining = 1

                elif revealedDoor + selection == 3:
                    remaining = 0

                else:
                    print("error")

                while True:
                    val = input(
                        "Do you want to swap to door {} ? y/n ".format(remaining)
                    )

                    if val == "y" or val == "yes":
                        selection = remaining

                        break

                    elif val == "n" or val == "no":
                        break

                    else:
                        print("invalid response.")

        if selection == prize:
            print("\nYOU WON!!! Prize was in door {} ".format(prize))

            wins += 1

            trueWins += 1

        else:
            print("Sorry, you lost. Prize was in door {} ".format(prize))

        print_doors(selection=[selection], prizeDoor=prize)

        trials += 1

        val = input("Play again? y/n ")

        if val == "y" or val == "yes":
            continue

        else:
            return (wins, trials, trueWins, trueTrials)


def monty_hall_helper_auto(swap, evil=False, blind=False):

    wins, trials, trueWins, trueTrials = 0, 0, 0, 0

    for _ in range(1000):
        prize = random.randint(0, 2)

        selection = random.randint(0, 2)

        if not evil or prize == selection:
            if blind:
                revealedDoor = choice([i for i in range(3) if i != selection])

            else:
                revealedDoor = choice(
                    [i for i in range(3) if i not in [selection, prize]]
                )

            if revealedDoor != prize:
                trueTrials += 1

                remaining = [i for i in range(3) if i not in [selection, revealedDoor]][
                    0
                ]

                if swap:
                    selection = remaining

                if selection == prize:
                    trueWins += 1

        if selection == prize:
            wins += 1

        trials += 1

    return (wins, trials, trueWins, trueTrials)


def monty_hall():

    variant = (
        input(
            "What type of host would you like to play against? Traditional (t), Evil (e), or Blind (b)? "
        )
        .strip()
        .lower()
    )

    mode = input("How would you like to play? Manual (m) or Auto (a)? ").strip().lower()

    wins, trials, trueWins, trueTrials = 0, 0, 0, 0

    if mode == "a":
        swap = input("Swap when prompted? y/n ").strip().lower()

        wins, trials, trueWins, trueTrials = monty_hall_helper_auto(
            swap in ("y", "yes"), evil=(variant == "e"), blind=(variant == "b")
        )

    elif variant == "e":
        wins, trials, trueWins, trueTrials = monty_hall_helper_manual(evil=True)

    elif variant == "b":
        wins, trials, trueWins, trueTrials = monty_hall_helper_manual(blind=True)

    else:
        wins, trials, trueWins, trueTrials = monty_hall_helper_manual()

    if trials > 0:
        print(
            "You won: {} out of {} times, or {}%".format(
                wins, trials, int(round(wins / trials, 2) * 100)
            )
        )

        if trueTrials:
            print(
                "If we only consider the games where a losing door was revealed, "
                "you won: {} out of {} times, or {}%".format(
                    trueWins, trueTrials, int(round(trueWins / trueTrials, 2) * 100)
                )
            )

    else:
        print("You didn't play. :(")


monty_hall()
