n = int(input('n : '))
m = int(input('m : '))


def Snake(n, i):
    s = ''
    for j in range(int(n/2)):
        if(i % 2) != 0:
            s += '#*'
        else:
            s += '*#'
    if(n % 2) != 0:
        if(i % 2) != 0:
            s += '#'
        else:
            s += '*'
    return s


for i in range(m):
    print(Snake(n, i))
