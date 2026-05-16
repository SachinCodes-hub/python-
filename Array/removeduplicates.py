# two pointers approach 

# one pointer for replacing the cuurent element . other for iterating over whole list for replacing and including every element in the array 

l = 1

# we will iterate over the list by the r pointer .
nums = [1,2,3,3,3,4,4,5]

for r in range(1 , len(nums)):
    if nums[r] != nums[l-1]:
        nums[l] = nums[r]
        l = l + 1
    

print(l) # l pointer will stop at the point wherew the remaingn elements will all be duplicates so if you want the no on unique elements return l . 
# l pointer is at teh last unique element . 

    