def compress(chars):
    s= 0 
    i= 0
    while i<len(chars):
        l = chars[i]
        count= 0
        while i<len(chars) and chars[i]==l:
            count +=1
            i += 1
        chars[s]= l
        s+=1
        if count>1:
            for c in str(count):
                chars[s]= c
                s+=1
    return s

chars = ["a"]
print(compress(chars))