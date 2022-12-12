from colorama import Back, Style

n = int(input('n : '))
m = int(input('m : '))

print(' X ', end=' ')

for i in range(m):
    print(Back.YELLOW, i+1, end=' ')
print(Style.RESET_ALL)

for i in range(n):
    for j in range(m):
        if j == 0:
            print(Back.YELLOW, i+1, end=' ')
            print(Style.RESET_ALL, '', end='')
        if i == j:
            print(Back.YELLOW, (i+1)*(j+1), end=' ')
            print(Style.RESET_ALL, end='')
        elif j+1 == m:
            print('',(i+1)*(j+1), ' ')
        else:
            print('',(i+1)*(j+1), end=' ')
