import itertools
for l in range(4):
    
    for i in itertools.product('0123456789', repeat=l):
        k = ''.join(i)
        for n in range(10):
            s = '3' + str(n) + '1' + k + '57'
            if int(s) % 2023 == 0:
                print(int(s), int(s) // 2023)
