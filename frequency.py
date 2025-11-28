dictionary={'ronaldo':2,'is':2,'the':2,'GOAT':1}
k=2
res=0
for key in dictionary:
    if dictionary[key]==k:
        res=res+1
print("frequency of k is "+str(res))
