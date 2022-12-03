
n = int(input('tedad daneshjo :'))
score = []

for i in range(n):
    print(('nomre daneshjo {} : ').format(i+1))
    s = float(input())
    score.append(s)

print('avarage : ', sum(score)/len(score))
print('max : ', max(score))
print('min : ', min(score))
