str= "()"
mapping = {"(":")",
           "[":"]",
           "{":"}"}

stack = ["i"]

#for i in str:
 #   if i in mapping:
  #      stack.append(i)
   # elif i in mapping.keys():
    #    in not stack or mapping[i]

#print(mapping["("])

print(stack.pop())
