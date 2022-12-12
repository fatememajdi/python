a = int(input('Number1 : '))
b = int(input('Number2 : '))

i = 1
while True:
    if a > b:
        if (a*i) % b == 0:
            print('KMM : ', a*i)
            break
    else:
        if (b*i) % a == 0:
            print('KMM : ', b*i)
            break
    i += 1
