string1 = "HelloWorld"
string2 = "HelloWorld123"
string3 = "Hello World"
string4 = "Hello World!"
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

print(string1.istitle())  # Output: False
print(string2.istitle())  # Output: False
print(string3.istitle())  # Output: True
print(string4.istitle())  # Output: True

print(string13.isspace())  # Output: True
print(string14.isspace())  # Output: False
print(string15.isspace())  # Output: False

