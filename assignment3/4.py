num = ''
numbers = []
while num != 'exit':
    num = input('number : ')
    if num != 'exit':
        numbers.append(float(num))

print('sum : ', sum(numbers))
