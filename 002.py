"""
In the question we were given a maze in which we start from north west and we have to go south east. 
there is another player, who has already traveled a path and we cannot follow the same path.
suppose p have already travelled A->B then we cannot travel A->B although we can visit A or B...
My solution is that if we cannot travel the same path why not travel completely opposite path?
since the grid is n*n , in the process we will also ensure that we do not go out of the grid.

e.g: 
EESES will become SSESE,,, all easts will be replaced by south and all south will be replaced by east.
"""

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
    print('Case #{}: {}'.format(i+1, npath))
