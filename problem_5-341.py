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
for N in range(12, 100):
    if N % 12 == 0:
        R = int_base(N, 12) + int_base(N, 12)[-2:]
    else:
        R = int_base(N, 12) + int_base((N % 12) * 9, 12)
    R = int(R, 12)
    if R > 300:
        min_R = min(R, min_R)
print(min_R)

