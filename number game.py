import random
playing=True
number=str(random.randint(10,20))
print("i will generate a number between 10 and 20 and you have to guess the number")
while playing:
    guess=input("give me your best guess")
    if number==guess:
        print("you won the game")
        break
    else:
        print("you guessed it wrong")
        
