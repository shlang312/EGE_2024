def triple(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s

def sum_num(n):
    s = 0
    N = int(n)
    for k in range(len(n)):
        s += (N//10**k) % 10
    if s % 3 == 0:
        return True
    return False
N_max = -10**6

for N in range(11, 100):
    R = triple(N)
    if sum_num(R):
        R = '20' + R
    else:
        R = '10' + R
    if int(R, 3) < 100:
        N_max = max(N_max, N)
        
print(N_max)

