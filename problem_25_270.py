def quantity_of_dividers(n):#для полных квадратов
    k = -1
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            k += 2
    return k

a = []
for k in range(21, 33):
    if quantity_of_dividers(k**6) == 7:
        a.append(k**6)
print(a)
#[148035889, 594823321, 887503681]
