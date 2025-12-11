import random
import time
number=random.randint(1,100)
def intro():
    print('may i ask your name')
    global name
    name=input()
    print(name+",we are going to play a game.i am thinking of a number between 1 and 100")
    if(number%2==0):
        x='even'
    else:
        x='odd'
        print("\nthis is a{} number".format(x))
        time.sleep(.5)
        print('go ahead and guess')
def pick():
    guessestaken=0
    while guessestaken<6:
      time.sleep(.25)
      enter=input("guess")
      try:
          guess=int(enter)
          if guess<=100 and guess>=1:
              guessestaken=guessestaken+1
              if guessestaken<6:
                if guess<number:
                    print("the guess of the number you have entered is too low") 
                if  guess>number:
                  print("the guess of number you have entered is too high")
                if guess !=number:
                   time.sleep(.5)
                   print('try again')
                if guess==number:
                   break
          if guess>100 or guess<1:
             print('the number is not correct')
             time.sleep(.25)
             print('please enter a number between 1 and 100')
      except:
         print('i dont think that '+enter+'is a number')
    if guess==number:
       guessestaken=str(guessestaken)
       print('good job,{}!,you have guessed the number in{}guesses{}!'.format(name,guessestaken))
    if guess!=number:
       print('the number i was thinking of was '+str(number))
playagain="yes"
while playagain=='yes' or playagain=='y' or playagain=='Yes':
   intro()
   pick()
   print('do you want to playa again')
   playagain=input()
                
