import itertools
for l in range(4):
    
    for i in itertools.product('0123456789', repeat=l):
        k = ''.join(i)
        for n in range(10):
            s = '123' + str(n) + '4' + k + '5679'
            if int(s) % 4013 == 0:
                print(int(s), int(s) // 4013)
