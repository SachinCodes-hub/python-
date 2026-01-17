#Doubly linked list will have address of prec node also . 
# prev val next 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
    
node1 = Node(5)
node2 = Node(4)
node3 = Node(6)
node1.next = node2
node2.next = node3 
node2.prev = node1
node3;prev = node2
