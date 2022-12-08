str1 = str(input('your string : '))
str2 = 'hello'
res = ''

i = 0

for char in str2:

    if(str1.find(char) != -1):
        res += char
        i = str1[i:].find(char)
        str1 = str1.replace(str1[:i], '')


if(res == str2):
    print('Yes')
else:
    print('No')
