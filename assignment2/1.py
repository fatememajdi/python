import math
import operator

operations = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.truediv,
              'sin': math.sin, 'cos': math.cos, 'tan': math.tan
              }

op = str(input('Operator : '))


if op == '+' or op == '-' or op == '/' or op == '*':
    num1 = float(input('Number 1 : '))
    num2 = float(input('Number 2 : '))
    print('{} {} {} = {}'.format(num1, op, num2, operations[op](num1, num2)))
elif op == 'sin' or op == 'cos' or op == 'tan':
    angle = float(input('angle : '))
    print('{} {} = {}'.format(op, angle, operations[op](math.radians(angle))))
elif op == 'cot':
    angle = float(input('angle : '))
    print('cot {} = {}'.format(angle, 1/(math.tan(math.radians(angle)))))
elif op == 'radical':
    num = float(input('Number : '))
    print('radical {} = {}'.format(num, (math.sqrt(num))))
elif op == 'factorial':
    num = float(input('Number : '))
    print('factorial {} = {}'.format(num, (math.factorial(num))))
