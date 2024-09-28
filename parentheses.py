def parentheses(str):
    pairs ={")":"(", "}":"{", "]":"["}
    stack= []
    for i in str:
        if i in pairs.values():
            stack.append(i)
        elif i in pairs.keys():
            if not stack or pairs[i] != stack.pop():
                return False
            
    return not stack

str = input("Enter the string : ")
print(parentheses(str))