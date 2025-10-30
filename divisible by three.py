def cube(number):
    return number*number*number
def three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(three(27))
print(three(28))
