
name = "Pulastya"
age = 36
weight = 71.8

intro1 = f"My name is {name}. I am {age} years old"
# Output: My name is Pulastya. I am 36 years old"

intro2 = "My name is {}. I am {} years old".format(name, age)
# Output: My name is Pulastya. I am 36 years old"

intro3 = "My name is {}. I am {} years old".format(name, age, weight)
# Output: My name is Pulastya. I am 36 years old"

intro4 = "My name is {}. I am {} years old and my weight is {} kgs".format(name, age)
# IndexError: Replacement index 2 out of range for positional args tuple

intro5 = "My name is %s. I am %d years old" % (name, age)
# Output: My name is Pulastya. I am 36 years old"

intro6 = "My name is %s. I am %d years old and my weight is %s kgs" % (name, age, weight)
# Output: My name is Pulastya. I am 36 years old and my weight is 71.8 kgs"

intro7 = "My name is %s. I am %d years old" % (name, age, weight)
# TypeError: not all arguments converted during string formatting

intro8 = "My name is %s. I am %d years old and my weight is %s kgs" % (name, age)
# TypeError: not enough arguments for format string


