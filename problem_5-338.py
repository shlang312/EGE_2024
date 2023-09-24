def int_base(n, base): # 10 => 45
    s = ''
    while n != 0:
        if n % base > 9:
            s = chr(n % base + 55) + s
        else:
            s = str(n % base) + s
        n //= base
    return s

def base_to_int(n, base): # 45 => 10
    s = 0
    for i in range(len(n)):
        if n[i].isdigit():
            s += int(n[i]) * base**(len(n) -i - 1)
        else:
            s += (ord(n[i]) - 55) * base**(len(n) -i - 1) 
    return s

min_R = 10**6
for N in range(1000, 10000):
    even, odd = 0, 0
    R = int_base(N, 45)
    for i in range(len(R)):
        if i % 2 == 0:
            even += base_to_int(R[i], 45)
        else:
            odd += base_to_int(R[i], 45)
    R = int_base(min(even, odd), 45) + R + int_base(max(even, odd), 45)
    R = base_to_int(R, 45)
    min_R = min(min_R, R)
print(min_R)
        
