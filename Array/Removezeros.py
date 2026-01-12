#remove no of zeros and put them in end .

nums = [1,2,0,56,0,4]

freqmap = {}

for i in range(0 , len(nums)):
    freqmap[nums[i]] = freqmap.get(nums[i] , 0 ) + 1
    
nums2 = []
for key in freqmap:
    if key != 0 :
        nums2.append(key)
    

for i in range(0 , freqmap[0]):
    nums2.append(0)
        
        
print(nums2)
    

#Try to find optimal solution - 
arr = [1,2,3,0,3,0]
n = len(arr)
for i in range(0 , n-1):
        if arr[i] ==0 and arr[i+1] != 0:  # here when their is 0 it will skip that part and that would be incorrect so . think about that case and add condition .
            arr[i] ,arr[i+1] = arr[i+1] , arr[i]
    
print(arr)


#try 2 - optimal solution - O(N)

tang = [1,2,0,2,0,4,3]
t = len(tang)
low = 0 
high = t-1 
while low < high:
    if tang[low] == 0 and tang[high] != 0 :
        tang[low] ,tang[high] = tang[high], tang[low]
    
    elif tang[low] != 0:
        low = low +1
    
    else:
        high = high -1
    
    
    
print(tang) 
