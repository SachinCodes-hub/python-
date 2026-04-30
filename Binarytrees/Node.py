#if we want to create binary tree first we need to create the nodes later we can connext them and create binary tree

# Node in binary tree 

class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None


#create nodes for each value

drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
tea = Node("tea")
coffee = Node("coffee")
cola = Node("cola")
fanta = Node("fanta")

# connect them as your binary tree - reations
hot.left = coffee
hot.right = tea 
cold.left = cola
cold.right = fanta

drinks.left = hot
drinks.right = cold

"""
        drinks 
        
        hot.    cold'

        tea coffee cola fanta
"""

# now our binary tree is created . 

print(drinks.right.right.val) # fanta

print(hot.left.val) # coffee