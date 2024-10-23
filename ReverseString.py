def ReverseString(s):
    l=s.strip().split(" ")
    l.reverse()
    return " ".join(l)


s = "  hello world  "
print(ReverseString(s))