def triple(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s

def even_odd(n: str):
    even = 0 # чет
    for x in n: # n - string
        if int(x) % 2 == 0:
            even += 1
    return 2*even > len(n)

min_R = 10**8

for N in range(11, 100):
    R = triple(N)
    if even_odd(R):
        R = '22' + R
    else:
        R = '11' + R
    if int(R, 3) > 100:
        min_R = min(min_R, int(R, 3))
        
print(min_R)
