def Occurence(haystack,needle):
    if haystack < needle:
        return -1
    for i in range(len(haystack)):
        if haystack[i:len(needle)]== needle:
            return 0
    return -1

haystack = "leetcode"
needle = "leeto"

print(Occurence(haystack,needle))