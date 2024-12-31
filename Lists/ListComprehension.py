
numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]  # squares becomes [1, 4, 9, 16, 25]
even_squares = [x**2 for x in numbers if x % 2 == 0]  # even_squares becomes [4, 16]

print(squares)                     # Output: [1, 4, 9, 16, 25]
print(even_squares)                # Output: [4, 16]

new_squares = [x**2 for x in range(1,6)]  # new_squares becomes [1, 4, 9, 16, 25]
odd_squares = [x**2 for x in range(1,6,2)]  # odd_squares becomes [1, 9, 25]

print(new_squares)                 # Output: [1, 4, 9, 16, 25]
print(odd_squares)                 # Output: [1, 9, 25]


