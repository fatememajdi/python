array = []

size = int(input('length of array :'))
for i in range(size):
    x = int(input('next value :'))
    array.append(x)

sortArray = array[:]
sortArray.sort()

if sortArray == array:
    print('Yes')
else:
    print('No')
