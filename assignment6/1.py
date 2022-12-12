import math

print('ax^2 + bx + c = 0')

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

delta = (b*b)-(4*(a*c))

if delta > 0:
    print('X1 : ', (-b + math.sqrt(abs(delta))) / (2 * a))
    print('X2 : ', (-b - math.sqrt(abs(delta))) / (2 * a))
elif delta == 0:
    print('X : ', -b / (2 * a))
else:
    print('X1 : ', - b / (2 * a), " + i", math.sqrt(abs(delta)))
    print('X2 : ', - b / (2 * a), " - i", math.sqrt(abs(delta)))
