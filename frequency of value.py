dictionary={"a":1,"b":1,"c":1,"d":2}
k=1
res=0
for key in dictionary:
    if dictionary[key]==k:
        res=res+1
print('the frequency of k is '+str(res))