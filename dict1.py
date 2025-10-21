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
