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

def f(N):
    even, odd = 0, 0
    R = int_base(N, 80)
    for i in range(len(R)):
        if base_to_int(R[i], 80) % 2 == 0:
            even += base_to_int(R[i], 80)
        else:
            odd += base_to_int(R[i], 80)
    #print(even, odd)
    R = R + int_base(max(even, odd), 80)[-1:]
    R = base_to_int(R, 80)
    return R

min_N = 10**8
for N in range(1, 1000):
    if f(f(N)) > 10**6:
        min_N = min(min_N, N)
print(min_N)

        
