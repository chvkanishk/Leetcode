class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key 

class Binary_tree:
    def __init__(self,root):
        self.root = Node(root)
    
    def insert(self,key):
        new_node=Node(key)
        if not self.root:
            self.root= new_node
            return new_node
        
        current = self.root
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
        return self.root 
    
    def inorder(self,root):
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
    
    def is_similar(self,p,q):
        q1=[p]
        q2= [q]

        while q1 and q2:
            node1= q1.pop(0)
            node2 = q2.pop(0)

            if (node1 is not None and node2 is None) or (node1 is None and node2 is not None):
                return False
            if node1 is not None and node2 is not None:
                if node1.value != node2.value:
                    return False 
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
            
        return not q1 and not q2



t1= Binary_tree(2)
t1.insert(1)
t1.insert(3)


print(t1.inorder(t1.root))