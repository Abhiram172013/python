try:
    age=int(input("please enter your age:"))
    if age<=0:
        print("age cannot be Zero or less than zero")
    else:
        print("your age is ",age)
        if age%2==0:
            print("your age is even")
        else:
           print("your age is odd")
except ValueError:
        print("invalid")
