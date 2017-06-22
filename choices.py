start = '''
You are walking through the woods with your dog spot. Suddenly he sees a squiral and the next thing you know you are
getting pulled through a graveyard up to a scary looking house.  Standing on the doorstep, you are unsure of what to do...
'''


print(start)


print("Type 'ring' to ring the doorbell or 'enter' to turn the doorknob and enter the house without asking.")
user_input = input()
if user_input == "ring":
    print("You decide to ring the doorbell and a Skeleton opens the door for you. Type 'go' to go with him or 'run' to leave the house immediatly.") # finished the story by writing what happens
    user_input = input()
    if user_input == "go":
        print("you decide to go with the skeleton and he turns out to be really nice and gives you a tour of his home. You become BESTIES!!!")
    elif user_input == "run":
        print("You decide to run for your life and hope to escape the graveyard with the creepy ghosts. THE END")
    else:
        print("Incorrect input!  Try again.")
elif user_input == "enter": #elif means else if
    print("You choose to enter the house, but as soon as you step through the door, you fall through a trap door in the floor. Type 'escape' to try and free yourself or 'stay' to accept your fate.") # finished the story writing what happens
    user_input = input()
    if user_input == "escape":
        print("You are able to break free but get lost in the mansion and DIE!!! THE END")
    if user_input == "stay":
        print("You decide to stay in the dungeon and the skeleton comes to get you and forces you to leave. THE END")
else:
    print("Incorrect input!  Try again.")
