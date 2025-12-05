s1={1,2,3,4}
s2={'a','b','c','d'}
s3=list(zip(s1,s2))
print(s3)

list1=[1,2,3,4,5]
list2=[2,4,6,7,8]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks=['reliance','bajaj','microsoft']
prices=[1234,5678,2345]
newdict={stocks:prices for stocks,prices in zip(stocks,prices)}
print('\n{}'.format(newdict))