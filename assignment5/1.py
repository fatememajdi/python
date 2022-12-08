phrase = str(input('ebarat ra vared koned : '))
array = []
for i in range(len(phrase)):
    if(i % 2) == 0:
        array.append(phrase[i])
phrase = ''
array.sort()
for i in range(len(array)):
    phrase += array[i]
    if(i != len(array)-1):
        phrase += ' + '

print(phrase)
