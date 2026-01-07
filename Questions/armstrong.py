sum = 0 
N = 1534
num = N
nod = len(str(N))
while num > 0 :
    ld = num % 10
    sum = sum +ld**nod
    num = num //10

if sum == N:
    print("is armstrong")
else:
    print("not an armstrong")
    