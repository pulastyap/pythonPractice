# For learning if conditional statement
user_count = int(input("How many numbers you want to print? "))

for num in range(user_count):
    if num % 2 == 1:
        continue
    print(num)
