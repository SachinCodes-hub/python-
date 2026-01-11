arr = [23,2,5,6,33,4]

largest = float("-inf")
second = float("-inf")
for _ in arr:
    if _ > largest:
        second = largest
        largest = _
        
        

print(largest , second)