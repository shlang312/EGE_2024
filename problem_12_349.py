def f(n):
    while '71' in n or '72' in n or '73' in n:
        if '71' in n:
            n = n.replace('71', '227')
        if '72' in n:
            n = n.replace('72', '37')
        if '73' in n:
            n = n.replace('73', '17')
        return n
