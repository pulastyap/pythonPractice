
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

user_num = int(input("Enter a positive number for which you want factorial: "))


result = factorial(user_num)

print(result)

# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
# 4! = 4 * 3 * 2 * 1 = 4 * 3!