class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    

node1 = Node(5)
node2 = Node(7)
node3 = Node(10)


node1.next = node2
node2.next = node3

print(node1.next.val) 


# append element to the linked list 

class singlylinkedlist:
    
    def __init__(self):
        self.head = None
    
    def append(self,val): # append value at the last position
        newnode = Node(val)
        if self.head == None:
            self.head == newnode
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = newnode
    
    

sll = singlylinkedlist()
sll.append(20)
print(sll)
                