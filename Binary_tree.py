class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key 

def insert(root,key):
    new_node = Node(key)

    if root is None:
        return new_node
    
    current = root
    parent = None

    while current:
        parent = current 
        if key < current.value:
            current = current.left
        else:
            current = current.right
        
    if key < parent.value:
        parent.left= new_node
    else:
        parent.right = new_node
    return root 


def inorder(root):
    current = root
    stack = []
    result = []

    while True:

        while current:
            stack.append(current)
            current = current.left 
        
        if not stack:
            break 
        
        current = stack.pop()
        result.append(current.value)

        current = current.right
    return result

root = Node(50)

insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print(inorder(root))