def sieve(n):
    prime = [True] * n
    s = []
    prime[0], prime[1] = False, False
    for i in range(2, n):
        if prime[i]:
            s.append(i)
            for j in range(2*i, n, i):
                prime[j] = False
    return s
def prime(n):
    return all([n % d != 0 for d in range(2, int(n**0.5)+1)])

s = sieve(10**6)
p = []
for i in range(len(s) - 1):
    if s[i + 1] - s[i] - 1 >= 90:
        print(s[i], prime(s[i]), s[i + 1], prime(s[i+1]))
        
        
        
'''"
360653 360749
370261 370373
396733 396833
492113 492227
604073 604171
838249 838349
860143 860239
927869 927961
"'''
