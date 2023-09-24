def sorted_numbers(n):
    a = []
    for k in range(len(str(n))):
        a.append(n // 10**k % 10)
    return a

max_k_min_n = []
K, M = '', ''
min_N = 10**6
max_K = -1 * min_N
for N in range (1000, 10000):
    num_N = sorted_numbers(N)
    num_N.sort()
    for x in num_N:
        M = M + str(x)
        K = str(x) + K
    R = int(K) - int(M)
    if R == 6174:
        if int(K) > max_K:
            max_K = int(K)
            max_k_min_n.append([max_K, N])
            
    K, M = '', ''
for i in range(len(max_k_min_n)):
    if max_k_min_n[i][0] == max_K:
        print(max_k_min_n[i][1])
    
