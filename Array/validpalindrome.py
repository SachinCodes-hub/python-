str = 'Tango charlie'
import re
lower = str.lower()
print(lower)

str1 = re.sub(r'[^a-z0-9]',"",str.lower()) # except the a - z and 0 - 9 remove everything removees the alphanumeric characeters . makes it a continous string 

print(str1)


n = len(str1)
left = 0 
right = n - 1
validpalindrome = "True"


while left <= right:
    if str1[left] != str1[right]:
        validpalindrome = "False"
    
    else:
        left = left + 1
        right = right -1
    

print(validpalindrome)