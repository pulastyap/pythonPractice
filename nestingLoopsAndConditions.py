person_age = int(input("Enter your age: "))

young_age_start = 18
old_age_start = 60

if person_age >= young_age_start:
    if person_age <= old_age_start:
        print("You are young")

choice_number = int(input("Choose a number less than 5: "))
"""
*
**
***
****
"""

for i in range(choice_number):
    for j in range(i+1):
        print("*", end="")
    print()

    
