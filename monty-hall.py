import random
from random import choice

def print_doors(selection = [], goat=[], win = []):
    ans = ["?","?","?"]
    selection_list =  ["","",""]
    
    for door in win:
        ans[door] = "$" 
    if len(win) > 0:
        for i in range(len(ans)):
            if i not in win:
                ans[i] = "X"
    else:
        for door in goat:
            ans[door] = "X"  
            
    print("|{}| |{}| |{}|\n 0   1   2".format(ans[0],ans[1],ans[2]))

    if len(selection) > 0:
        selection_list[selection[0]] = "^"
        print("{}    {}     {}".format(selection_list[0],selection_list[1],selection_list[2]))


def monty_hall_helper_manual(evil = False):
    wins = 0
    trials = 0
    while True:
        doors = [0,0,0]
        prize = random.randint(0,2)
        doors[prize] = 1
        print_doors()
        while True:
            selection = input("Select door 0,1, or 2\n")
            try:
                selection = int(selection) 
            except:
                print("invalid selection.")
                continue
            if selection < 0 or selection >2:
                continue
            else:
                break
        if not evil or prize == selection:
            reveal = choice([i for i in range(0,3) if i not in [selection, prize]])
            print_doors(selection = [selection])
            print("Surprise! The host revealed that the prize is not behind door {}".format(reveal))
            print_doors(selection = [selection], goat=[reveal])
            if reveal + selection == 1:
                remaining = 2
            elif reveal + selection == 2:
                remaining = 1
            elif reveal + selection == 3:
                remaining = 0
            else:
                print("error")
            while True:
                val = input("Do you want to swap to door {} ? y/n ".format(remaining))
                if val == "y" or val =="yes":
                    selection = remaining
                    break
                elif val =="n" or val =="no":
                    break
                else:
                    print("invalid response.")
        if selection == prize:
            print("\nYOU WON!!! Prize was in door {} ".format(prize))
            wins +=1
        else:
            print("Sorry, you lost. Prize was in door {} " .format(prize))
            print_doors(win=[prize], goat=[selection,reveal])
        print_doors(selection = [selection], win=[prize])
        trials +=1
        val = input("Play again? y/n ")
        if val == "y" or val =="yes":
            continue
        else:
            return (wins,trials)

def monty_hall_helper_auto(swap):
    wins = 0
    trials = 0
    for i in range(1000):
        doors = [0,0,0]
        prize = random.randint(0,2)
        doors[prize] = 1
        selection = random.randint(0,2)
        reveal = choice([i for i in range(0,3) if i not in [selection, prize]])
        if reveal + selection == 1:
            remaining = 2
        elif reveal + selection == 2:
            remaining = 1
        elif reveal + selection == 3:
            remaining = 0
        val = swap
        if swap:
            selection = remaining            
        if selection == prize:
            wins +=1
        trials +=1
    return (wins,trials)
    
def monty_hall(): 
    style = input("Would you like to play traditionally (1) run a simulation (2), or try against an evil host (3)?\n ")
    if style == "1":
        win, trials = monty_hall_helper_manual()
    elif style == "2":
        swap = input("Do you want the computer to swap when prompted? y/n")
        if swap == "y" or swap =="yes":
            win, trials = monty_hall_helper_auto(True)
        else:
            win, trials = monty_hall_helper_auto(False)
    elif style == "3":
        win, trials = monty_hall_helper_manual(evil = True)

    
    if(trials > 0):    
        print("You won : {} out of {} times, or {} %".format(win, trials, win/trials))
    else:
        print("You didn't play. :(")
    
    
    
monty_hall()
