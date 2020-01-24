t = int(input())

for i in range(t):
    n = input()
    path = input()
    npath = ''
    for j in path:
        if j == 'E':
            npath += 'S'
        else:
            npath += 'E'
    print('Case #{}: {}'.format(i+1,npath))