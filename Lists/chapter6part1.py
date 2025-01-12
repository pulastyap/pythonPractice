square = [1, 4, 9, 16, 25]

square_new = [x ** 2 for x in range(1, 1000) if x % 100 == 0]

print(square_new)