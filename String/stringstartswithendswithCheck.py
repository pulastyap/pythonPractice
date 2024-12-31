

string9 = "hello World"

print(string9.startswith("hello"))            # Output: True
print(string9.startswith("Hello"))            # Output: False
print(string9.startswith("World"))            # Output: False
print(string9.startswith("World", 6))         # Output: True
print(string9.startswith("World", 6, 9))      # Output: False
print(string9.startswith(("hel", "Hel")))     # Output: True

print(string9.endswith("rld"))                # Output: True
print(string9.endswith("rlD"))                # Output: False
print(string9.endswith("hello"))              # Output: False
print(string9.endswith("lo", 0, 5))           # Output: True
print(string9.endswith("lo", 0, 6))           # Output: False
print(string9.endswith(("rld", "RLD")))       # Output: True

