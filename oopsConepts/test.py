class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name, 'is', self.age, 'years old.')

person1 = Person('Arti', 35)

person1.details()