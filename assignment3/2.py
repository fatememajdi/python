import random

number = random.sample(range(1, 7), 1)
print(number[0])

while number[0] == 6:
    number = random.sample(range(1, 6), 1)
    print('yoho :) : ', number[0])
