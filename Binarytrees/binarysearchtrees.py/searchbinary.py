# search in binary tree 

temp = root
val = 10
while temp is not None:
    if temp.val == val:
        
        print(temp) 
    elif temp > val:
        temp == temp.left
    
    else:
        temp = temp.right

#return None # if nothing is found