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
            while curr.next != None:  # append . you have to be on last element so hence . when im on last curr = last ,  stop there . so for stopping there curr.next is None
                curr = curr.next
            curr.next = newnode
        
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        
        else:
            curr = self.head
            while curr != None:  #here we dont have to stop . we dont want our curr to be on last element so their is no need. 
                
                print(curr.val, end = " ")
                curr = curr.next
            
    def insertat(self,val , postion):
        newnode = Node(val)
        prevnode = None
        
        if postion ==0:
            newnode.next = self.head
            self.head = newnode
        
        else:
            count =0 
            curr = self.head
            while curr.next !=0 and count <postion:
                prevnode = curr
                curr = curr.next
                count +=1 
            
            prevnode.next = newnode
            newnode.next = curr
            
    def delete(self, val):
        temp = self.head

    # Case 1: Empty list
        if temp is None:
            print("List is empty")
            return

    # Case 2: Head needs to be deleted
        if temp.val == val:
            self.head = temp.next
            return

    # Case 3: Delete non-head node
        prev = None
        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

    # Case 4: Value not found
        print("Node not found")
                    
            
            
                
            
        

sll = Singlylinkedlist()

sll.append(20)
sll.append(12)
sll.append(16)
sll.insertat(5,0)
sll.traverse()
sll.delete(16)
sll.traverse()
print(sll)
            
        
    