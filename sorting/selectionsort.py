#Selection sort - here we select the min or max element through iteration and swap it with the minindex element .
#so wll always update the min value in the case of ascending order and max in case of descending order.




nums = [5,3,2,7,6,8]
n = len(nums)

for i in range(0, n):
    minindex = i
    for j in range(i+1, n):
        if nums[j] < nums[minindex]:
            nums[minindex],nums[j] = nums[j],nums[minindex]
        
print(nums)