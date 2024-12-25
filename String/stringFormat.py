first_name = "Pulastya"
last_name = "Pandey"
age = 36

full_name = "{} {}. I am {} years old".format(first_name, last_name, age)
full_name2 = "%s %s. I am %d years old" % (first_name, last_name, age)
full_name1 = f"{first_name} {last_name}. I am {age} years old"
print(full_name)
print(full_name1)
print(full_name2)