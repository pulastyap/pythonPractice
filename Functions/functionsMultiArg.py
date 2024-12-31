# For learning if conditional statement

def product(*nums):
    product = 1
    for num in nums:
        product *= num
    return product

def user(**key_value):
    for key, value in key_value.items():
        print(f"{key}: {value}")


multiply = product(1,2,3,4)

print(f"The product result is {multiply}")
user(name="Pulastya", age=36, country="USA")