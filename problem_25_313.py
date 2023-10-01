'3?1*57'
'100000000'
'3x1yzt57'
a = []
for x in range(10):
    s = int('3' + str(x) + '157')
    if s % 2023 == 0:
        a.append(s)
    for y in range(10):
        s = int('3' + str(x) + '1' + str(y) + '57')
        if s % 2023 == 0:
            a.append(s)
        for z in range(10):
            s = int('3' + str(x) + '1' + str(y) + str(z) + '57')
            if s % 2023 == 0:
                a.append(s)
            for t in range(10):
                s = int('3' + str(x) + '1' + str(y) + str(z) + str(t) + '57')
                if s % 2023 == 0:
                    a.append(s)
a.sort()
for x in a:
    print(x, x // 2023)
