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

def q_of_factors(n):
    k = -1 # полные квадраты
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            k += 2
    return k

def max_factor(n):
    max_d = -10**6
    for d in range(int(n**0.5), n):
        if n % d == 0:
            max_d = max(max_d, d)
    return max_d

a = []
for i in range(10000, 22361 ):
    n = i**2
    if q_of_factors(n) == 9:
        a.append(n)

for i in range(5):
    print(a[len(a) - i - 1], max_factor(a[len(a) - i - 1]))
    

    

'''
499835449 6327031
499701316 249850658
499656609 166552203
499343716 249671858
499164964 249582482
'''
