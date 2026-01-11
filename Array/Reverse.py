def reverse(arr , left , right):
    if left >right:
        return
    else:
        arr[left],arr[right] = arr[right], arr[left]
        reverse(arr , left+1 , right -1)
    
    return arr 
    
    
print(reverse([1,2,4,5,34,2] ,0 , 5))
        