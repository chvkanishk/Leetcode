def twoSum(num,target):
    
    for i in range(len(num)):
        #find= 0
        find = int(target)- num[i]
        if find in num and num.index(find) != i:
            return [i,num.index(find)]
        else:
            continue
    return []

print("Enter the numbers in the list")
num=[]
while True:
    x=input("Enter")
    if x=="":
        break
    else:
        num.append(int(x))
print(num)

target= input("Enter the target")

print(twoSum(num,target))
    


