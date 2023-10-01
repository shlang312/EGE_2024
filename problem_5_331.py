def invert(n):
    n = n.replace('1', '5')
    n = n.replace('0', '1')
    n = n.replace('5', '0')
    return(n)

def double(n):
    s = ''
    for x in n:
        s += x*2
    return s

min_N = 10**6
for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 2 != 0:
        R = invert(R)
    R = double(R)
    R = int(R, 2)
    if R > 60:
        min_N = min(min_N, N)
print(min_N)
    
