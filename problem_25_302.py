def mask(n):
    if str(n)[0] == '9' and str(n)[2:5] == '979' and str(n)[-1] == '8' and '0' in str(n):
        return True
    return False

for k in range(1, 199729):
    n = k*50068
    if mask(n):
        print(n, k)

'''
9097906348 181711
9297928008 185706
'''
    
