weight = float(input('weight :'))
height = float(input('height :'))

mbi = weight/(height * height)

if mbi < 18.5:
    print('underweight')
elif 18.5 <= mbi <= 24.9:
    print('normal')
elif 25 <= mbi <= 29.9:
    print('overweight')
elif 30 <= mbi <= 34.9:
    print('obese')
elif 35 <= mbi:
    print('extremely obese')
