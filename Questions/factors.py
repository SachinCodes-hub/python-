num = 36 
factors = []
for i in range(1,num+1):
    if num %i == 0 :
        factors.append(i)
    else:
        continue

print(factors)


factors2 = []

for i in range(1 ,num//2+1):
    if num%i == 0 :
        factors2.append(i)
    else:
        continue
    
factors2.append(num)

print(factors2)

factors3 = []
import math
sqrt = math.sqrt(num)
for i in range(1 ,int(sqrt)+1):
    if num%i == 0:
        factors3.append(i)
        if num//i != i :
            factors3.append(num//i)
        else:
            continue

print(factors3)