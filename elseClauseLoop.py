choice_number = int(input("Choose a number less than 5: "))


for i in range(choice_number):
    for j in range(i+1):
        print("*", end="")
    print()

else:
    print("Pattern printed")

num = 0
while num < choice_number:
    if num == 2:
        break
    print(num)
    num += 1

else:
    print("While loop completed")