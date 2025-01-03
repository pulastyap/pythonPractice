
student = {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8, 'height': 5.7, 'sal': 40}
student_keys = student.keys()
print(student_keys)                     # Output: dict_keys(['name', 'age', 'grade', 'weight', 'height', 'sal'])
print(type(student_keys))               # Output: <class 'dict_keys'>

student_values = student.values()       
print(student_values)                   # Output: dict_values(['Pulastya', 36, 'B', 71.8, 5.7, 40])
print(type(student_values))             # Output: <class 'dict_values'>

student_items = student.items()
print(student_items)                    # Output: dict_items([('name', 'Pulastya'), ('age', 36), ('grade', 'B'), ('weight', 71.8), ('height', 5.7), ('sal', 40)])
print(type(student_items))              # Output: <class 'dict_items'>

student_city = student.setdefault("city", "Bangalore")
print(student_city)                     # Output: Bangalore
print(student)                          # Output: {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8, 'height': 5.7, 'sal': 40, 'city': 'Bangalore'}

student_name = student.setdefault("name", "Pandey")
print(student_name)                     # Output: Pulastya
print(student)                          # Output: {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8, 'height': 5.7, 'sal': 40, 'city': 'Bangalore'}

