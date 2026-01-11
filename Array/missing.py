arr = [1,2,3,5,7,8]
N = 8 
sum = N * (N+1) / 2
total = 0 
for num in arr:
    total = total + num
    
print(sum - total)