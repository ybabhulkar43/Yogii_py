def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)

res=fact(4)
print(res)