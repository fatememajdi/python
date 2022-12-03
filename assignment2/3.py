firstName = str(input('first name :'))
lastName = str(input('last name :'))
score = []


for i in range(3):
    print(('score {} : ').format(i+1))
    s = float(input())
    score.append(s)

avg = sum(score)/len(score)
if avg >= 17:
    print('Great')
elif 17 > avg >= 12:
    print('Normal')
else:
    print('Fail')
