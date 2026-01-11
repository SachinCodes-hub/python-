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


