def f(n):
    if n % 3 == 0:
        R = base_3(n)
        return int(R + base_3(n)[-2:], 3)
    else:
        R = base_3(n)
        return int(R + base_3(n % 3 * 5), 3)

    
def base_3(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s

min_R = 10**8

for N in range(1, 100):
    if f(N) > 133:
        min_R = min(min_R, f(N))
print(min_R)

        
