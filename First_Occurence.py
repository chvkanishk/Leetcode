def Occurence(haystack,needle):
    if haystack < needle:
        return -1
    for i in range(len(haystack)):
        if haystack[i:len(needle)]== needle:
            return i
    return -1


def Occ(haystack,needle):
    try:
        return haystack.index(needle)
    except ValueError:
        return -1

haystack = "hello"
needle = "ll"

print(Occ(haystack,needle))

