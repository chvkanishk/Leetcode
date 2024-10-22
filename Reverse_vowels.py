def reverse(s):
    l="aeiouAEIOU"
    m=[]
    for i in s:
        if i in l:
            m.append(i)
    n=len(m)
    s=list(s)
    for i in range(len(s)):
        if s[i] in l:
            n-=1
            s[i]=m[n]
    return "".join(s)
    

s = "IceCreAm"
print(reverse(s))