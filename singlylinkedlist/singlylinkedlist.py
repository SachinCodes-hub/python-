class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

class Singlylinkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,val):
        newnode = Node(val)
    
        if self.head == None:
            self.head = newnode
        
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newnode
        
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        
        else:
            curr = self.head
            while curr != None:
                print(curr.val, end = " ")
                curr = curr.next
            
            
        

sll = Singlylinkedlist()

sll.append(20)
sll.append(12)
sll.append(16)
sll.traverse()

print(sll)
            
        
    