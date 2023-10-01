a = []
for x in range(10):
    k = '1234' + str(x) + '5'
    if k not in a and int(k) % 2025 == 0:
                a.append(int(k))
    for y in range(10):
        m = '12' + str(y) + '34' + str(x) + '5'
        if m not in a and int(m) % 2025 == 0:
                a.append(int(m))
        for z in range(10):
            n = '12' + str(y) + str(z) + '34' + str(x) + '5'
            if n not in a and int(n) % 2025 == 0:
                a.append(int(n))
a.sort()
for x in a:
    print(x, x // 2025)
'''
"1253475 619
12103425 5977
12593475 6219
12913425 6377"
'''
