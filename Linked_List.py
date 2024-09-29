class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def Delete(self,key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node= current_node.next

        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None
        
    def Display(self):
        current_node= self.head
        while current_node:
            print(current_node.data,end= " -> ")
            current_node = current_node.next
        print("None")

