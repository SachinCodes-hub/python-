#Binary search 

#iterative - 
"""
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



"""

target3 = 45

nums = [1,2,34,2,15,44,45,3,3]

n = len(nums)

low = 0 
high = n -1
mid = (low + high ) // 2
while low < high:
    
    if nums[mid] == target3:
        print(nums[mid]) # index of the target
        break
    else:
        if nums[mid] > target3:
            high = mid - 1
        else:
            low = mid + 1 
    
    
        
    