def gcd(str1,str2):
    i=0
    j=0
    r=[]
    while i<len(str1) and j<len(str2):
        if str1[i] == str2[j]:
            r.append(str2[i])
    return r















str1 = "ABCABC"
str2 = "ABC"

print(gcd(str1,str2))