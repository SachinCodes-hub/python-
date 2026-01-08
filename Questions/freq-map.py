freqmap = {}
nums = [1,2,3,3,4,5,4]
n = len(nums)

for i in range(0 , n):
    if nums[i] in freqmap:
        freqmap[nums[i]] += 1 #here what this does is it will get the value of nums[i] in the frequency map if dosnot exist in the dictonary. it will add the elemnty
        
    else:
        freqmap[nums[i]] = 1
    
print(freqmap[5]) # for getting the number of occurance of nums[i]

list = [1, 2,3 ,4 ,5,4 ]
hashmap = {}
n = len(list)
for i in range (0 , n):
    hashmap[list[i]]  = hashmap.get(list[i] , 0) +1 # only in hash map where you can use hashmap.get , it get value of that elemnet in the dict if not it will return 0 . 
    #this is advanced statement where like freq map you dont have to write if else , ypu can just get the value of that elemnt 
print(hashmap[4]) #hash map[element]
        
    


#Hashing in python .
#statement - prestoring the values somewhere and again using them . 

num1 =[1,2,4,5,6,4 ,5,8 , 9 ]
num2 = [2,3,1,5,66,8]

for num in num1: # here the TC = O(N *M) we are iterating one by on e
    count = 0 
    for tang in num2:
        if tang == num :
            count +=1
        
        else:
            continue
    print(count)
    

# optimal solution . Hashing

hashlist = [0] *11

for num in num1:
    hashlist[num] +=1 

for tango in num2:
    if tango >10 or tango <1:
        print("-1")
    else:
        print(hashlist[tango])