"""
def function():
       # base condition
          return
          
       
       fuction()
    
 
"""


def factorial(N):
    if N ==0 or N==1:
        return N
    
    return N * factorial(N-1)

print(factorial(5))


#fabonacci num - return the index of the number

def fab(num):
    if num ==0 or num ==1:
        return num
    return fab(num-1) +fab(num-2)

print(fab(8)) #Returns the index of the faonacci .

#string is plaindrome or not 

def ispalindrome(str , left , right):
    if left >right:
        return       #base condition 
    
    if str[left] != str[right]:
        return False
    return True
    ispalindrome(str , left +1 , right-1)
    
    
    
print(ispalindrome("mom" ,0 ,2))