#rotate by one place - Slicing 
num = [1,2,4,5,6,4]
n = len(num)
num[:] =  [num[n-1]] + num[0:n-1] #good line as it converts the num[n-1] to list , and slice all other element till n - 2
print (num)

#Rotate sorted array by one place - actual approach - 

num2 = [1,2,3,42,2,3,2]
n = len(num2)

last = num2[n-1]# store the last element . 

print(last)

for i in range(n-2,-1,-1): #reverse iteration form n-2 to 1 st index 
    num2[i+1] = num2[i]
    
num2[0] = last # updates the first element

print(num2)


#Rotate by k places .

#here the catch is k can be anything k%N = rotations . actual rotaions that you would have to do . 

num3 = [1,2,3,4,5]
k = 17 
n = len(num3)
rotations = k % n

for i in range(0 , rotations):# n th enumber of roattion , n times we would have to get the last elemnet put it first . 
    
    l = num3.pop()
    num3.insert(0,l)

print(num3)








#optimal solution by slicing . O(N)

K = k %n # why this agin this will be the catull no of shiftings  and u notice the solution  wat has happedn as you just to add 2 slices togetherr form n-k + till n-k
nums = [1,2,3,4,5,7]
nums[:] = nums[n-K:] +nums[0:n-K]
print(nums)