nums = [4,3,2,7,8,9]
#Bubble sort - swap adjasant element like compare them and swap  . 

n = len(nums)
for i in range(n-2 ,-1 , -1):
    for j in range(0 , i+1):
        if nums[j+1] < nums[j]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
        
print(nums)


#Descending order
arr = [6,4,2,1,8,5]

for i in range(n-2, -1,-1):
    for j in range(0 , i+1):
        if arr[j+1] >arr[j]:
            arr[j], arr[j+1] = arr[j+1],arr[j]
        
print(arr)
