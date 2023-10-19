def int_base(n, base):
    s = ''
    while n != 0:
        s = str(n % base) + s
        n //= base
    return s
def F(N):
    R = int_base(N, 2)
    if N % 3 == 0:
        R = R + '010'
    else:
        R = R + int_base((N % 3) * 5, 2)
    return int(R, 2)

min_R = 10**6
n1 = 0
for N in range(10,10000):
    if int(F(N)) % 2 == 0 and int(F(N)) > 300:
        if int(F(N)) < min_R:
            n1 = N
            min_R = F(N)
print(n1)
    

        
