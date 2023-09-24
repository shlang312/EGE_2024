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
for N in range(15, 100):
    if N % 15 == 0:
        R = str(N) + int_base(N, 15)[:2]
    else:
        R = str(N) + int_base((N % 15) * 13, 15)
    R = int(R, 15)
    if R > 700:
        min_R = min(R, min_R)
print(min_R)

