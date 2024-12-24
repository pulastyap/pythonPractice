# For learning if conditional statement
user_count = int(input("How many numbers you want to print? "))

for num in range(user_count):
    print(num)

fruits = []

while True:
    user_fav_fruit = input("What is your favourite fruit? (Enter 'None' to stop entering): ")
    if user_fav_fruit != "None":
        fruits.append(user_fav_fruit)
    else:
        break

for fruit in fruits:
    print(fruit)