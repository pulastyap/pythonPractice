year = int(input("Please choose a year: "))

if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0): print(f"Entered year {year} is a leap year.")
else: print(f"Entered year {year} is not a leap year.")