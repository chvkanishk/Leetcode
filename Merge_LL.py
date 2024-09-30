from Linked_List import LinkedList



def Merge(l1,l2):
    merged_list= LinkedList()

    c1=l1.head
    c2= l2.head
    while c1 and c2:
        if c1.data <= c2.data:
            merged_list.append(c1.data)
            c1=c1.next
        else:
            merged_list.append(c2.data)
            c2= c2.next
    
    while c1:
        merged_list.append(c1.data)
        c1= c1.next
    while c2:
        merged_list.append(c2.data)
        c2= c2.next
    
    return merged_list




list1= LinkedList()
list2 = LinkedList()

list1.append(1)
list1.append(2)
list1.append(4)

list2.append(1)
list2.append(3)
list2.append(4)

mergell= LinkedList()
mergell=Merge(list1,list2)
mergell.Display()

