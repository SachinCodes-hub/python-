nums = [[1,2,3],[2,3,4],[5,5,3]]

print(nums)

rows = len(nums)
coloums = len(nums[0])
'''
for i in range(0 , rows):        #Representation of matrix
    for j in range(0 , coloums):
        if j > i :
            nums[i][j] = 0 
        
print(nums)

'''

for i in range(0 , rows):
    for j in range(0 , coloums):
        print(nums[i][j] , end = " ")
    print()
    
    
result = [[0]*rows for i in range(coloums)] 
print(result)

for i in range(0,rows):
    for j in range(0,coloums):
        result[j][i] = nums[i][j]
    

for i in range (0,rows):
    for j in range(0,coloums):
        print(result[i][j] , end = " ")