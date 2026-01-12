#Maximum sum of subarray - Continuous

arr = [-1,2,3,-4,-2,1,1]
maxsum = float("-inf")

for i in range(0 , len(arr)):
    sum = arr[i]
    for j in range(i+1 , len(arr)):
        sum = sum + arr[j] 
        if sum <0:
            break
        maxsum = max(sum , maxsum)
        

print(maxsum)
        
#tc - O(N ^2) #sc - O(1)

#optimal solution
maxtotal = float("-inf")
total = 0 
for i in range(0 , len(arr)):
    total = total + arr[i]
    maxtotal = max (total,maxtotal)
    
    if total < 0 :
        total = 0    #Here whenever total is negative . there is no point in continuing with the negative .instead reset it to 0 then agin continue
        #Negative total will not get us to the maximum total 
    
print(maxtotal)
    