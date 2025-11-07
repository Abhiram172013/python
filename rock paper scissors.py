import random
while True:
    useraction=input("enter a choice:rock,paper or scissors")
    possibleactions=["rock","paper","scissors"]
    computeraction=random.choice(possibleactions)
    if useraction==computeraction:
        print("its a tie")
    elif useraction=="rock":
        if computeraction=="scissors":
            print("you win")
        else:
            print("you lose")
    elif useraction=="paper":
        if computeraction=="rock":
            print("you win")
        else:
            print("you lose")
    elif useraction=="scissors":
        if computeraction=="paper":
            print("you win")
        else:
            print("you lose")
    playagain=input("do you want to play again")
    if playagain!="yes":
     break



