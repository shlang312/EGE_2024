a = []
for x in range(10):
    k = '2468' + str(x) + '35'
    if k not in a and int(k) % 13 == 0:
                a.append(int(k))
    for y in range(10):
        m = '24' + str(y) + '68' + str(x) + '35'
        if m not in a and int(m) % 13 == 0:
                a.append(int(m))
        for z in range(10):
            n = '24' + str(y) + str(z) + '68' + str(x) + '35'
            if n not in a and int(n) % 13 == 0:
                a.append(int(n))
a.sort()
for x in a:
    print(x, x // 13)
