'''
student = {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8, 'height': 5.7, 'sal': 40}
student.clear()
print(student)   

empty_item = {}
empty_item.clear()
print(empty_item)





student = {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8, 'height': 5.7, 'sal': 40}
last_item = student.popitem()
print(last_item)            # Output: ('sal', 40)
print(student)              # Output: {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8, 'height': 5.7}

last_item = student.popitem()
print(last_item)            # Output: ('height', 5.7)
print(student)              # Output: {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8}

empty_item = {}
last_item = empty_item.popitem()
print(last_item)            # KeyError: 'popitem(): dictionary is empty'


student = {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8, 'height': 5.7, 'sal': 40}
grade = student.pop("grade")
print(grade)                # Output: B
print(student)              # Output: {'name': 'Pulastya', 'age': 36, 'weight': 71.8, 'height': 5.7, 'sal': 40}

default_value = student.pop("address", "Bangalore")    
print(default_value)                # Output: Bangalore
print(student)                      # Output: {'name': 'Pulastya', 'age': 36, 'weight': 71.8, 'height': 5.7, 'sal': 40}
address = student.pop("address")    # KeyError: 'address'



student = {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8, 'height': 5.7, 'sal': 40}
del student["age"]
print(student)              # Output: {'name': 'Pulastya', 'grade': 'B', 'weight': 71.8, 'height': 5.7, 'sal': 40}

del student["address"]      # KeyError: 'address'



student = {'name': 'John', 'age': 21, 'grade': 'A'}
student["weight"] = 71.8
print(student)          # Output: {'name': 'John', 'age': 21, 'grade': 'A', 'weight': 71.8}

student["grade"] = "B"
print(student)          # Output: {'name': 'John', 'age': 21, 'grade': 'B', 'weight': 71.8}

updated_student = [('name', 'Pulastya'), ('height',  5.7)]

student.update(updated_student)
print(student)          # Output: {'name': 'Pulastya', 'age': 21, 'grade': 'B', 'weight': 71.8, 'height': 5.7}

updated_student = {'age': 36, 'sal': 40}

student.update(updated_student)
print(student)          # Output: {'name': 'Pulastya', 'age': 36, 'grade': 'B', 'weight': 71.8, 'height': 5.7, 'sal': 40}

'''

student = {'name': 'John', 'age': 21, 'grade': 'A'}
print(student.get("address", "Bangalore"))      # Output: Bangalore

