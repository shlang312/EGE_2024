import itertools
c = 0
def mask(n):
    if n[0] == '8' and n[-2:] == '06' and '80' in n[1:-2]:
        return True
    return False
c = 0
for k in range(1, 1960000):
    n = k*4546
    if mask(str(n)):
        if c % 60 == 0:
            print(n, n // 4546)
        c += 1
            
                
