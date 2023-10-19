import itertools

def mask(n):
    if str(n)[0] == '2' and  str(n)[2:6] == '5432' and str(n)[-1] == '1' and '9' in str(n):
        return True
    return False

for x in range(10):
    for r in range(4):
            for j in itertools.product('0123456789', repeat=r):
                k = ''.join(j)
                s = '2' + str(x) + '5432' + k + '1'
                if int(s) % 1017 == 0 and '9' in s:
                    print(int(s), int(s) // 1017)

'''
2254325931 2216643
2454329151 2413303
2554320591 2511623
2954327031 2904943
'''
