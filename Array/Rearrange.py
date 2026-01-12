num = [2,3,-2,5,-7,-8]
pos= []
neg = []
for i in range(0,len(num)):
    if num[i] > 0:
        pos.append(num[i])
    else:
        neg.append(num[i])
    
print(pos,neg)

for i in range(0 , len(num)):
    if i %2 ==0:
        num[i] = pos[i]
    else:
        num[i] = neg[i]
    
print(num)