arr = [1,32,3,4,5]
sorted = True

for i in range(0 , len(arr) - 2):
    if arr[i] >= arr[i+1]:
        sorted = False
    

print(sorted)

