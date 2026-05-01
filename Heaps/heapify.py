nums = [10 , 7 , 6, 4 , 5 , 4 , 5 , 6 , 2 ]



arr = nums 
ind = 5
val = 9
def heapifyDown(arr , ind):              # heapify down function
    N = len(arr)

    largest_ind = ind
   

    leftchild_ind = 2 * ind + 1
    rightchild_ind = 2 * ind  + 2


# if the left child holds larger value , update the largest index 

    if leftchild_ind < N and arr[leftchild_ind] > arr[largest_ind]:
        largest_ind = leftchild_ind

# if the right child holds larger value , update the largest index 

    if rightchild_ind < N and arr[rightchild_ind] > arr[largest_ind]:

        largest_ind = rightchild_ind

# if largest is not the current index , swap and hepify down  - this will get executed till we get the largest index as current index . 

    if largest_ind != ind: # ind - curent index value
        arr[largest_ind] , arr[ind] = arr[ind] , arr [largest_ind] # swaping the elements 
        heapifyDown(arr , largest_ind)



def heapifyup(arr , ind ):          # heapify up function
    Parent_ind = (ind - 1 ) // 2 # integer division coz index

# if current index holds larger value than the parent

    if ind > 0 and arr[ind] > arr[Parent_ind]:
      arr[ind] , arr[Parent_ind] = arr[Parent_ind] , arr[ind]
      heapifyup(arr , Parent_ind)




#logic code for max heap - heapify algorithm

if nums[ind] > val :
    nums[ind] = val
    heapifyDown(arr , ind)

else:
    nums[ind] = val
    heapifyup(arr , ind)
    



def heapifyDown(self , arr , ind):              # heapify down function
    N = len(arr)

    largest_ind = ind
   

    leftchild_ind = 2 * ind + 1
    rightchild_ind = 2 * ind  + 2


# if the left child holds larger value , update the largest index 

    if leftchild_ind < N and arr[leftchild_ind] > arr[largest_ind]:
        largest_ind = leftchild_ind

# if the right child holds larger value , update the largest index 

    if rightchild_ind < N and arr[rightchild_ind] > arr[largest_ind]:

        largest_ind = rightchild_ind

# if largest is not the current index , swap and hepify down  - this will get executed till we get the largest index as current index . 

    if largest_ind != ind: # ind - curent index value
        arr[largest_ind] , arr[ind] = arr[ind] , arr [largest_ind] # swaping the elements 
        self.hepifyDown(arr , largest_ind)



def heapifyfup(self , arr , ind ):          # heapify up function
    Parent_ind = (ind - 1 ) // 2 # integer division coz index

# if current index holds larger value than the parent

    if ind > 0 and arr[ind] > arr[Parent_ind]:
      arr[ind] , arr[Parent_ind] = arr[Parent_ind] , arr[ind]
      self.heapifyup(arr , Parent_ind)





print(arr[2]) # crazy scenes after applying the heapify algorithm the the value 9 will be at 2 nd index to satisgfy the max heap 


# remember the we can apply it in max heap , when we want to insert a index at its correct position keeping the binary tree rules alive then we have to use this heapify algorithm . 

 
