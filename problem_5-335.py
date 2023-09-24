def sum_num(n):
    c0, c1, c2, c3 = map(int, [n[0], n[1], n[2], n[3]])
    s = str(min(c0+c3, c1+c2)) + str(max(c0+c3, c1+c2))
    return int(s)

def base_8(n):
    s = ''
    while n != 0:
        s = str(n % 8) + s
        n //= 8
    return s

min_N, max_N = 10**6, -10**5

for N in range(512, 4096):
    if sum_num(base_8(N)) == 317:
        min_N, max_N = min(min_N, N), max(max_N, N)
print(min_N + max_N)
        
