def int_base(n, base):
    s = ''
    while n != 0:
        if n % base > 9:
            s = chr(n % base + 55) + s
        else:
            s = str(n % base) + s
        n //= base
    return s

min_N = 10**6
for N in range(1, 10000):
    N_sixteen = int_base(N, 16)
    N1 = N
    if N % 2 == 0:
        N //= 2
    else:
        N -= 1
    if N % 6 == 0:
        N //= 6
    else:
        N -= 1
    if N % 15 == 0:
        N //= 15
    else:
        N -= 1
    R = N
    if R == 523 and 'C' in N_sixteen:
        min_N = min(min_N, N1)
print(min_N)
        
