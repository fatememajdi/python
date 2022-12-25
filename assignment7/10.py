lst1 = [1000, 500, 600, 700, 5000, 90000, 17500]
print(list(map(lambda item: item+2000, list(filter(lambda item: item < 8000, lst1)))))
