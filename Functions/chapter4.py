
def area_of_square(side):
    return side ** 2

def print_square_area(side, type_of_square):
    print("Area of", type_of_square, "square", area_of_square(side))


side_length = int(input("Enter the side of Square: "))

print_square_area(side_length, "small")
print_square_area(side_length + 1, "medium")
print_square_area(side_length * 3, "big")