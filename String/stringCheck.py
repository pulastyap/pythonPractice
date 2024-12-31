string1 = "HelloWorld"
string2 = "HelloWorld123"
string3 = "Hello World"
string4 = "12345"
string5 = "123abc"
string6 = "hello world"
string7 = "helloworld"
string8 = "hello12world"
string9 = "hello World"
string10 = "hello-world"
string11 = "HELLO-WORLD"
string12 = "123HELLOWORLD"
string13 = "   \t\n"
string14 = " hello "
string15 = "" 

print(string9.endswith("rld"))            # Output: True
print(string9.endswith("rlD"))            # Output: False
print(string9.endswith("hello"))            # Output: False
print(string9.endswith("lo", 0, 5))         # Output: True
print(string9.endswith("lo", 0, 6))         # Output: False
print(string9.endswith(("rld", "RLD")))     # Output: True

'''
print(string9.startswith("hello"))            # Output: True
print(string9.startswith("Hello"))            # Output: False
print(string9.startswith("World"))            # Output: False
print(string9.startswith("World", 6))         # Output: True
print(string9.startswith("World", 6, 9))      # Output: False
print(string9.startswith(("hel", "Hel")))     # Output: True


print(string13.isspace())  # Output: True
print(string14.isspace())  # Output: False
print(string15.isspace())  # Output: False

print(string1.istitle())  # Output: False
print(string2.istitle())  # Output: False
print(string3.istitle())  # Output: True

print(string1.isalpha())  # Output: True
print(string2.isalpha())  # Output: False
print(string3.isalpha())  # Output: False

print(string3.isalnum())  # Output: False
print(string2.isalnum())  # Output: True

print(string4.isdigit())  # Output: True
print(string5.isdigit())  # Output: False

print(string6.islower())  # Output: True
print(string7.islower())  # Output: True
print(string8.islower())  # Output: True
print(string9.islower())  # Output: False
print(string10.islower())  # Output: True

print(string3.isupper())  # Output: False
print(string11.isupper())  # Output: True
print(string12.isupper())  # Output: True
'''