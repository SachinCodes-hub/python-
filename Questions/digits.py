n = 12321
num = n
count = 0 
result = 0 

while num > 0:
    ld = num%10
    count +=1
    result = result *10 +ld
    num = num //10

if n ==result:
    print("ispalindrome")
else:
    print("not a palindrome")

print(count)