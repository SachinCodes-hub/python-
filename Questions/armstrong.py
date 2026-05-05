sum = 0 
N = 1534
num = N
nod = len(str(N))
while num > 0 :
    ld = num % 10
    sum = sum +ld**nod # gets you the sum of the number
    
    num = num //10

if sum == N:
    print("is armstrong")
else:
    print("not an armstrong")



# function for getting to know if the number if armstrong of not 


def isarmstrong(num):
    N = num
    str1 = str(num)
    NOD = len(str1)
    sum = 0 
    while N > 0 :
        ld = N % 10 
        sum = sum + ld**NOD 
        N = N //10
    
    if num == sum:
        return True
    else:
        return False
    

print(isarmstrong(153))