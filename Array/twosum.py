
#Two pointer approach
arr = [5 ,6,2,3,4,5,6]
target = 11
n = len(arr)
for i in range(0 , n):
    for j in range(i+1 ,n):
        if arr[i] +arr[j] == target :
            print(i ,j)
        
        else:
            continue
    


#optimal solution

hashmap = {}
n = len(arr)
for i in range(0 , n):
    remaining = target - arr[i]
    
    if remaining in hashmap:
        print(hashmap[remaining] ,i)
    
    hashmap[arr[i]] = i

    
