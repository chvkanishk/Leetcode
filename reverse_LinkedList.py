from Linked_List import LinkedList

def reverseList(self, head):
        prev = None 
        current =head
        while current is not None:
            next_node= current.next
            current.next = prev
            prev = current
            current= next_node
        return prev

list1= LinkedList()

list1.append(1)
list1.append(2)
list1.append(4)

list2 =LinkedList()
list2 = reverseList(list2)