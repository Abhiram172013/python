import array as arr
arraynum=arr.array('i',[1,2,3,4,5,3,2,3])
print("original array is "+str(arraynum))
print("number of the occurences of the number 3 in the array is"+str(arraynum.count(3)))
arraynum.reverse()
print("the reversed array is ")
print(str(arraynum))

      
