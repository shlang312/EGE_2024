def f(n):
    if n <= 5:
        return n
    elif n % 3 == 0:
        return n + f(n / 3 + 2)

for n in range(1, 10000):
    try:
        a = f(n)
        if a > 1000:
            print(n)
    except:
        continue
