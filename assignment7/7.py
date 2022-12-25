from functools import reduce
Fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                 range(n-2), [0, 1])

n = int(input('number : '))
print('Fibonacci series upto ', n, ':',Fib(n))
