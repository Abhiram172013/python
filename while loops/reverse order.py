a=int(input("please enter a number "))
count=0
temp=a
while temp>0:
    temp//=10
    count+=1
print("total digits are: ",count)