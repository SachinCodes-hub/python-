str = "12344"
n = int(str)

sum = 0 
count = 0 
while n >0:
    count +=1
    ld = n %10
    sum = sum +ld 
    n = n //10

print(sum)