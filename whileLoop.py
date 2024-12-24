# For learning if conditional statement
user_count = int(input("How many numbers you want to print? "))
num = 0
while num < user_count:
    print(num)
    num += 1

fruits = []

while True:
    user_fav_fruit = input("What is your favourite fruit? (Enter 'None' to stop entering): ")
    if user_fav_fruit != "None":
        fruits.append(user_fav_fruit)
    else:
        break

num = 0
while num < len(fruits):
    print(fruits[num])
    num += 1