
keys = ["name", "age", "grade"]
values = ["John", 21, "A"]
student = dict(zip(keys, values))
print(student)          # Output: {'name': 'John', 'age': 21, 'grade': 'A'}

keys = ("name", "age", "grade")
values = ("John", 21, "A")
student = dict(zip(keys, values))
print(student)          # Output: {'name': 'John', 'age': 21, 'grade': 'A'}

student = dict(zip(values, keys))
print(student)          # Output: {'John': 'name', 21: 'age', 'A': 'grade'}

keys = ["name", "age",]
values = ["John", 21, "A"]
student = dict(zip(keys, values))
print(student)          # Output: {'name': 'John', 'age': 21}

keys = ["name", "age", "grade"]
values = ["John", 21,]
student = dict(zip(keys, values))
print(student)          # Output: {'name': 'John', 'age': 21}



'''
empty_dict = {}
print(empty_dict)       # Output: {}




# Creating an empty dictionary
my_dict = dict()            
print(my_dict)          # Output: {}

# Creating a dictionary with key-value pairs using keyword arguments
student = dict(name="John", age=30, city="New York")
print(student)          # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Creating a dictionary from a list of tuples
student_list = [("name", "John"), ("age", 30), ("city", "New York")]
student_dict = dict(student_list)
print(student_dict)      # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Creating a dictionary from a list of tuples
student_tuple = (("name", "John"), ("age", 30), ("city", "New York"))
student_dict = dict(student_tuple)
print(student_dict)      # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Creating a dictionary from another dictionary
new_student_dict = dict(student_dict)
print(new_student_dict)     # Output: {'name': 'John', 'age': 30, 'city': 'New York'}




student = dict(name= "John", age= 21, grade= "A")
print(student)
print(type(student))


student = {"name": "John", "age": 21, "grade": "A"}
stud_contact_details = {"name": "John", 
                        "contact no": {"mobile no": 2242242242,
                                       "home phone no": 4424424424},
                        "address": {"street address": "N ABC road",
                                    "unit no" : 100},
                                    "city" : "Chicago",
                                    "state": "IL",
                                    "zip code": 60010}

print(student)
print(type(student))
print(stud_contact_details)
print(type(stud_contact_details))
'''