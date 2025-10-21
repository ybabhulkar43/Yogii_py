l1=['Yogi','Rocky','Mahesh','Kinda']
l2=[1,2,3,4,5,6,7]
dict1={}
length=len(l1)
for i in range(length):
    dict1[l1[i]]=l2[i]

print('Dictionary is:',dict1)
#-------------------------------------------------------------------
t1=tuple(dict1.keys())
print('Tuple is:',t1)
#-----------------------------------------------------------------
dict1={l1:l2 for l1,l2 in zip(l1,l2)}
print('The Dictionary is:',dict1)

print('The Dict Items Are:')
for x in dict1:
    print(x,'--->',dict1[x])

print('The Dict Items Are(using for loop with value x and Y):')
for x,y in dict1.items():
    print(x,'--->',y)

