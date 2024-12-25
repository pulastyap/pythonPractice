score = int(input("Please enter your score: "))

if 100 >= score >= 90: print("Grade A")
elif 90 > score >= 80: print("Grade B")
elif 80 > score >= 70: print("Grade C")
elif 70 > score >= 60: print("Grade D")
elif 0 <= score < 60: print("Grade F")
else: print("Invalid Score")