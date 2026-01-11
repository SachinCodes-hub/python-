#remove duplicates form the sorted array . 
#Brute force

arr = [1,1,2,2,3,4,4,5,6]
freqmap ={}
arr1 = []
for i in range(0 , len(arr)):
    if arr[i] in freqmap:
        freqmap[arr[i]] += 1
    else:
        freqmap[arr[i]] = 1 
    

for key in freqmap:
    arr1.append(key)


for _ in arr:
    print(freqmap[_])
    

print(arr1)

#optimal - Two pointers 


    
