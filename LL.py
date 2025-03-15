class Node:
    def __init__(self,value):
        self.value=value
        self.next= None

class Linkedlist:
    def __init__(self):
        self.head =None
    
    def insert(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        new_tail = self.head

        while new_tail.next:
            new_tail= new_tail.next

        new_tail.next = new_node

    def display(self):
        a = self.head
        while a :
            print(a.value, end="->")
            a=a.next

        print("Null")

    def reverse(head):
        prev= None 
        current = head

        while current is not None:
            next_node= current.next
            current.next = prev
            prev = current
            current = next_node

        return prev 


v = Linkedlist()

v.insert(1)
v.insert(2)
v.insert(3)
v.display()





