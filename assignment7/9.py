text = 'Winter Olympics in 2022 will take place in Beijing China'


def removeVowels(char):
    if char in 'aeiou':
        return False
    else:
        return True


print(text)
print(''.join(filter(removeVowels, text.lower())))
