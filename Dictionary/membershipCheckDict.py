
student = {'name': 'Pulastya', 'age': 36, 'grade': 'B',}

print("name" in student)                            # Output: True
print("address" in student)                         # Output: False
print("name" in student.keys())                     # Output: True

print("Pulastya" in student.values())               # Output: True
print(("name", "Pulastya") in student.items())      # Output: True
print(("name", "Pandey") in student.items())        # Output: False

