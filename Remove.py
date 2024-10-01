def remove(num,val):
    j=0
    for i in range(len(num)):
        if num[i] != val:
            num[j]=num[i]
            j+=1
    return j

num= [0,1,2,2,3,0,4,2]
val = 2

print(remove(num,val))