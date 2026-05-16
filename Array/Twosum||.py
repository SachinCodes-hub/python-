nums = [2,3,4,5,6,9]

target = 7 

# number of solutions exists - the sum of the elements must be target. append the indices of all those pairs . constraints - O(N)


left = 0 
right = len(nums) - 1
result = []
while left < right:
    total = nums[left] + nums[right]
    
    if total == target :
        result.append([left,right])
        left = left + 1
        right = right - 1 
    
    else:
        if total > target :
            right = right - 1 
        
        else:
            left = left + 1 
        
    

print(result)
        
