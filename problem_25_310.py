def dividers(n):
    k = 0
    s = set()
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            s.add(d)
            s.add(n // d)
    return s

def sieve(n):
    prime = [1]*n
    s = []    
    prime[0], prime[1] = 0, 0
    for i in range(len(prime)):
        if prime[i] == 1:
            s.append(i)
            for j in range(2*i, n, i):
                prime[j] = 0
    return s

def max_factor(n):
    max_d = -10**6
    for d in range(int(n**0.5), n):
        if n % d == 0:
            max_d = max(max_d, d)
    return max_d


k = 0
n = 500000
while k != 5:
    s = sum(dividers(n))
    if str(s)[-2] == '7':
        print(n, s)
        k += 1
    n += 1
    
    
            
