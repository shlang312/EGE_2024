max_len = -10**6
for n in range(4, 1000):
    s = '1' + '2' * n
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
    max_len = max(max_len, len(s))
print(max_len)
