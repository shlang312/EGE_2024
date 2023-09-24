def int_base(n, base):
    s = ''
    while n != 0:
        if n % base > 9:
            s = str(chr(n % base + 55)) + s
        else:
            s = str(n % base) + s
        n //= base
    return s

min_R = 10**7
for N in range(5, 100):
    if N % 5 == 0:
        R = int_base(N, 5) + int_base(N, 5)[-2:]
    else:
        R = int_base(N, 5) + int_base((N % 5) * 7, 5)
    R = int(R, 5)
    if R > 200:
        min_R = min(R, min_R)
print(min_R)

