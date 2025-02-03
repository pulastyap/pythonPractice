class Student:
    __school_name = 'Kendriya Vidyalaya Dipatoli Ranchi'

    def __init__(self, name: str, cls: str, sec: str, roll: int):
        self.__name = name
        self.__cls = cls
        self.__sec = sec
        self.__roll = roll

    def get_name(self) -> str:
        return self.__name
    
    def get_school_name(self) -> str:
        return Student.__school_name
    
    def set_name(self, name: str):
        if name.isalpha():
            self.__name = name
        else:
            print('Name is not set!\nError: Name should contain only alphabets')

pulastya = Student('Pulastya', '10', 'A', 10)
arti = Student('Arti', '9', 'B', 11)


print(pulastya.get_name())
print(arti.get_name())
print(pulastya.get_school_name())
print(arti.get_school_name())

pulastya.set_name('Munmun ')
print(pulastya.get_name())

# pulastya_name = 'Pulastya'
# pulastya_class = '10'
# pulastya_sec = 'A'
# pulastya_roll = 10


# arti_name = 'Arti'
# arti_class = '9'
# arti_sec = 'B'
# arti_roll = 11


# def details(name, cls, sec, roll):
#     print(name, 'studies in class', cls, 'section', sec, 'and her/his roll number is', roll)

# details(arti_name, arti_class, arti_sec, arti_roll)

