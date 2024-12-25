user_num = int(input("Enter a positive number for which you want factorial: "))

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

result = factorial(user_num)

print(result)