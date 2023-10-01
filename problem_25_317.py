#*2?2
def prime_factors(n):
    d = []
    for x in range(2, int(n**0.5) + 1):
        while n % x == 0:
            d.append(x)
            n //= x
    if n != 1:
        d.append(n)
    return d

a = []
for n in range(100, 10000):
    if (n % 10 == 2) and (n // 100 % 10 == 2):
        if len(prime_factors(n)) == 7:
            #print(n)
            a.append([n, max(prime_factors(n))])
a.sort()
for x in a:
    print(*x)
            
