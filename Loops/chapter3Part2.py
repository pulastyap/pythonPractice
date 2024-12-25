# Write a program to get a number from user and print all numbers from 0 to given number minus 1

user_num = int(input("Choose a stop number: "))

for i in range(user_num):
    if i == 5:
        break
    print(i)

else:
    print("The Loop completed without break")
