import itertools
for k in range(4):
    for x in range(10):
        for i in itertools.product('02468', repeat=k):
            s = '123' + ''.join(i) + '45' + str(x) + '67'
            if int(s) % 257 == 0:
                print(s, int(s) // 257)
