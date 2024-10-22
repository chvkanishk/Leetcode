def gcdofstring(s1,s2):

    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    if s1+s2 != s2+s1:
        return ""
    len_gcd = gcd(len(s1),len(s2))
    r= s1[:len_gcd]
    return r















str1 = "ABABAB"
str2 = "ABAB"

print(gcdofstring(str1,str2))