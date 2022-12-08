txt = str(input('text : '))
if((sum(1 for char in txt if char.isupper())) > (sum(1 for char in txt if char.islower()))):
    print(txt.upper())
else:
    print(txt.lower())
