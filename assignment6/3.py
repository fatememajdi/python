a = int(input('Number1 : '))
b = int(input('Number2 : '))

aDivisor = []
bDivisor = []

for i in range(int(a/2)):
    if a % (i+1) == 0:
        aDivisor.append(int(i+1))
        aDivisor.append(int(a / (i+1)))

for i in range(int(b/2)):
    if b % (i+1) == 0:
        if i+1 in aDivisor:
            bDivisor.append(int(i+1))
        elif b / (i+1) in aDivisor:
            bDivisor.append(int(b / (i+1)))


print('BMM : ', max(bDivisor))
