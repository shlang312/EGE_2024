def binary(n):
    n_2 = bin(n)[2:]
    if n % 2 == 0:
        n_2 = n_2 + '0'
    else:
        n_2 = n_2 + '1'
    if n_2.count('1') % 2 == 0:
        n_2 = n_2 + '0'
    else:
        n_2 = n_2 + '1'
    return int(n_2, 2)
min_R = 10**6
for N in range(1, 1000):
    if binary(N) > 2023:
        min_R = min(min_R, binary(N))
print(min_R)
