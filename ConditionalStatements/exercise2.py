user_num = float(input("Please choose a number: "))

if user_num == 0:
    print(f"Entered number {user_num} is zero.")
elif user_num < 0:
    print(f"Entered number {user_num} is negative.")
else:
    print(f"Entered number {user_num} is positive.")