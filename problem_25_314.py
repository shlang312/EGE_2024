'1*2??76'
'100000000'
a = []
for x in range(10):
    for y in range(10):
        s = int('12' + str(x) + str(y) + '76')
        if s % 1923 == 0:
            a.append(s)
        for z in range(10):
            s = int('1' + str(z) + '2' + str(x) + str(y) + '76')
            if s % 1923 == 0:
                a.append(s)
            for t in range(10):
                s = int('1' + str(z) + str(t) + '2' + str(x) + str(y) + '76')
                if s % 1923 == 0:
                    a.append(s)
a.sort()
for x in a:
    print(x, x // 1923)
