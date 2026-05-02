n = 5 # number of nodes
m = 6  # edges 

edges = [[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]] # by this edges we know the connections between this nodes . 

# 1 based index graph

matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
print(matrix)

#editing our edges into the 0 element matrix 
for u,v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1
    
print(matrix) # output with the connections link value as 1 

#[[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0]]


# List

lst = [[] for _ in range(n+1)]

# print(lst) - # list approach is better as it use less stack space than matrix -

 


for u , v in edges:
    lst[u].append(v)
    lst[v].append(u) # vice - versa 

print(lst)



#Dictionary - not preferable -coz sometimes dict -will take o(N) sometimes it does its operations in O(1)

my_dict = {}

for i in range(1 , n + 1): # start form 1 
    my_dict[i] = [] # empty dict
    
    
for u , v in edges:
    my_dict[u].append(v) # key - u , value - v 
    my_dict[v].append(u) # vice versa - why this statement coz - when 1 is connected to 2 then common sense 2 is connected to 1 but code machine dosent know this unless you write it . 
    
print(my_dict)