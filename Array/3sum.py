#brute force

nums = [-1 , -2,2,1,0,3,2]
n = len(nums)
myset = set()
for i in range(0 , n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if nums[i] + nums[j] + nums[k] == 0:
                temp = [nums[i],nums[j],nums[k]]
                temp.sort()
                myset.add(tuple(temp))
                
            
for ans in myset:
    print(list(ans))

#TC - O(N^3) , SC  - O(N)

#better solution 
myset = set()
result = set()
for num in nums:
    myset.add(num)
    

for i in range(0 ,n):
    for j in range(i+1, n):
        third = -(nums[i]+nums[j])
        
        if third in myset:
            temp = [nums[i],nums[j],third]
            temp.sort()
            result.add(tuple(temp)) #here the result should be added to set , to remove the duplicates .set has only unique elements .
            
        
    
print(result)
        
        