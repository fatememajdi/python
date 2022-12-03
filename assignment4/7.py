number = int(input("Number :  "))


def isFactorial(number):
    factorial = i = 1
    while factorial < number:
        i += 1
        factorial *= i
    return factorial == number


if isFactorial(number):
    print('Yes')
else:
    print('no')
