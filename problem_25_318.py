#1x1 x - восьмизначное 1........1
def sum_digits(x):
    s = 0
    for i in range(len(str(x))):
        s += x // 10 ** i % 10
    return s
p = []
a = []
max_sum = -10**6
for x in range(1000001268, 1999999991, 2023):
    if x // 10**9 == 1 and x % 10 == 1:
        p.append(x)
for x in p:
    max_sum = max(max_sum, sum_digits(x))
for x in p:
    if sum_digits(x) == max_sum:
        a.append(x)
a.sort(reverse = True)
for x in a:
    print(x, x // 2023)


        
