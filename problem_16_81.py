def f(n):
    if n <= 5:
        return n
    elif n % 5 == 0:
        return n + f(n / 5 + 1)
    else:
        return n + f(n + 6)

for n in range(0, 1000):
    try:
        a = f(n)
        if a > 1000:
            print(n)
            break
    except:
        continue
