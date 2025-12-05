num1=[1,2,3,4,5]
num2=[1,2,3,4,5]
result=map(lambda x,y:x+y,num1,num2)
print("the addition of two lists ")
print(list(result))

num=[1,2,3,4,5]
def square(n):
    return n*n
square=list(map(square,num))
print("square of  numbers in list ")
print(square)