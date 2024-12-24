# For learning if conditional statement

def product(*args):
    product = 1
    for num in args:
        product *= num
    return product

def user(**kargs):
    for key, value in kargs.items():
        print(f"{key}: {value}")


multiply = product(1,2,3,4)

print(f"The product result is {multiply}")
user(name="Pulastya", age=36, country="USA")