def int_base(n, base):
    s = ''
    while n != 0:
        s = str(n % base) + s
        n //= base
    return s
def F(N):
    R = int_base(N, 2)
    if N % 3 == 0:
        R = R + R[-3:]
    else:
        R = R + int_base((N % 3) * 3, 2)
    return int(R, 2

max_R = -10**6
for N in range(10,10000):
    if int(F(N)) < 170:
        max_R = max(int(F(N)), max_R)
print(max_R)
    

        
