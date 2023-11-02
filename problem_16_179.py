import functools
@functools.lru_cache()
def f(n):
    if n < 2:
        return n
    else:
        return n % 2 + 10 * f (n//2)

print(int('100000100001000100101', 2))
