def prefix(str):
    if len(str) == 0:
        return ""
    ans= str[0]
    n=len(ans)

    for i in str[1:]:
        while ans != i[0:n]:
            n-=1
            if n==0:
                return ""
            ans= ans[0:n]
    return ans 

print("Enter the names in the list")
str=[]
while True:
    x=input("Enter")
    if x=="":
        break
    else:
        str.append(x)
print(str)

#str = ["flower","flow","flight"]
print(prefix(str))