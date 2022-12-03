n = int(input("tool mar ra vared konid :) "))

snake = ''

for i in range(int(n/2)):
    snake += '*#'

if(n % 2) != 0:
    snake += '*'

print(snake)
