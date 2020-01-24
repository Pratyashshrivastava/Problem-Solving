t = input()

for i in range(t):
    n = input()
    v = ''
    for j in n:
        if(j == '4'):
            v += '1'
        else:
            v += '0'
    n = n.replace('4','3')
    v = v.lstrip('0')
    print('Case #{}: {} {}'.format(i+1,n,v))
        