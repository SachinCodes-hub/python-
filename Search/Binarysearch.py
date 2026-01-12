#Binary search 

#iterative - 

arr = [1,2,3,7,4,5]

low = 0 
high = len(arr) -1 
target = 4
while low < high:
    mid = (low +high) //2
    if target ==arr[mid]:
        print(mid)
    
    elif target > arr[mid]:
        low = mid +1
    
    else:
        high = mid - 1
 

       
print(mid)