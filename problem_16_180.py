import functools
@functools.lru_cache()
def f(n):
    if n < 9:
        return n // 3 + n % 3
    else:
        return f(n // 9) + n // 3 + n % 3

k = 0
for n in range(9**7):
    if f(n) == 33:
        k += 1
print(k)
