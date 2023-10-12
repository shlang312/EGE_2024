def prime_factors(x):
    s = []
    for d in range(2, int(x**0.5) + 1):
        while x % d == 0:
            s.append(d)
            x //= d
    if x != 1:
        s.append(x)
    return s

def F(n):
    g = prime_factors(int(n))
    if len(g) == 2 and 2 in g:
        if all([sum(g) % d != 0 for d in range(2, int(sum(g)**0.5) + 1)]):
            return [n, sum(g)]
    return False


'''import itertools
for m in range(10):
    for k in range(2):
        for i in itertools.product('0123456789', repeat=k):
            for j in itertools.product('0123456789', repeat=k):
                s = int('12' + ''.join(i) + '4' + ''.join(j) + '8' + str(m))
                if s <= 10**7 and F(s) != False:
                    print(F(s))'''
            
                
'''
124282 62143
1204282 602143
1214182 607093
1224082 612043
1229482 614743
1244482 622243
1295482 647743
'''
import itertools
for k in range(0, 2):
        for i in itertools.product('0123456789', repeat=k):
            for j in itertools.product('0123456789', repeat=k):
                print(i, j)
