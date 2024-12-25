# For learning if conditional statement

def area_of_rectangle(length, width = 2):
    area = length * width
    circumference = 2 * (length + width)
    return area, circumference


l = float(input("Length of Rectangle: "))
w = float(input("Width of Rectangle: "))

area, circumference = area_of_rectangle(l)

print(f"Area and Circumference of Rectangle are {area} and {circumference}")