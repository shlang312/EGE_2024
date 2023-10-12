def dividers_mask(n):
    k = 0
    s = set()
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            s.add(d)
            s.add(n // d)
    for x in s:
        if str(x)[0] == '4':
            k += 1
    if k == 24:
        return True
    return False

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

for n in range(10**6, 5*10**5, -1):
        if dividers_mask(n):
            print(n, max_factor(n))
        
