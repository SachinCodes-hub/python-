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