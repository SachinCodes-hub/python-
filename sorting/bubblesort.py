nums = [4,3,2,7,8,9]
#Bubble sort - swap adjusunt element like comapere them and swap  . 

n = len(nums)
for i in range(n-2 ,-1 , -1):
    for j in range(0 , i+1):
        if nums[j+1] < nums[j]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
        
print(nums)