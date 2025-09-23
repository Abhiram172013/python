print("select your ride")
print("1.bike")
print("2.car")
choice=int(input("enter your choice"))
if choice==1:
    print("what type of bike")
    print("1.harley davidson")
    print("2.royal enfield")
    choice2=int(input("enter your choice"))
    if choice2==1:
        print("you have selected harley davidson")
    else:
        print("you have selected royal enfield")
elif choice==2:
    print("what type of car")
    print("1.buggatti chiron pur sport ")
    print("2.porsche 911 GT3 RS")
    choice3=int(input("enter your choice"))
    if choice3==1:
        print("you have selected buggatti ")
    else:
        print("you have selected porsche")
else:
    print("invalid input")