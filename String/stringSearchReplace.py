full_name = "Pulastya Pandey"

print(full_name.find("a"))                # Output: 3
print(full_name.find("a", 5))             # Output: 7
print(full_name.find("a", 4, 7))          # Output: -1
print(full_name.find("a", 4, 8))          # Output: 7
print(full_name.find("Pu"))               # Output: 0
print(full_name.find("Pa"))               # Output: 9
print(full_name.find("pa"))               # Output: -1
print(full_name.find(" "))                # Output: 8
print(full_name.rfind("a"))               # Output: 10
print(full_name.rfind("a", 5))            # Output: 10
print(full_name.rfind("a", 2, 8))         # Output: 7
print(full_name.rfind("Pu"))              # Output: 0
print(full_name.rfind("Pa"))              # Output: 9

print(full_name.replace("a", "e"))              # Output: Pulestye Pendey
print(full_name.replace("a", "e", 2))           # Output: Pulestye Pandey
print(full_name.replace("dey", "day", 2))       # Output: Pulastya Panday

