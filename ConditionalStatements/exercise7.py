# Write a program that asks the user for two numbers and an operator (+, -, *, /). 
# Perform the operation based on the input and display the result.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

ope = input("What operation you want to perform?\n1. + for addition\n2. - for subtraction\n3. * for multiplication\n4. / for float division\n    ")

result = 0

match ope:
    case "+":
        print("Result is", num1 + num2)
    case "-":
        print("Result is", num1 - num2)
    case "*":
        print("Result is", num1 * num2)
    case "/":
        print("Result is", num1 / num2)
    case _:
        print("Wrong operation entered")