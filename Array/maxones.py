arr = [1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1]
count = 0 
maxi = float("-inf")
for num in arr:
    if num == 1:
        count +=1
        maxi = max(count,maxi)
    else:
        count = 0 
    

print(maxi)

    