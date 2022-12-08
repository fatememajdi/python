txt = str(input('text : '))

if(txt.lower() == txt[::-1].lower()):
    print('palindrome')
else:
    print('not palindrome')
