def f(n):
    if n <= 5:
        return n
    elif n % 3 == 0:
        return n + f(n / 3 + 1)

for n in range(0, 1000):
    try:
        a = f(n)
        if a > 1000:
            print(n)
            break
    except:
        continue
