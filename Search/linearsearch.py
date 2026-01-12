#searching through one single iteration . - linear search
nums = [1,2,4,2,1,1,2]
target = 4 
for i in range(0,len(nums)):
    if nums[i]== target:
        print(i)
    

#TC - O(N) - SC _ O(1)