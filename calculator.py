def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
choice=input("please enter choice:a,b,c,d")
num1=int(input("enter the first number"))
num2=int(input("please enter the second number"))
if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='b':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='d':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid input")
