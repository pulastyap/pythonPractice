fruits = ['apple', 'banana', 'orange', 'grape']
animals = ('cat', 'dog', 'cow', 'fox')
animals1 = {'cat', 'dog', 'cow', 'fox'}
person = {"name": "Pulastya", "birth_place": "India", "current_place": "USA"}

print(",".join(fruits))         # Output: apple,banana,orange,grape
print(".".join(animals))        # Output: cat.dog.cow.fox
print("".join(animals1))        # Output: catdogcowfox
print("-".join(person.values()))        # Output: Pulastya-India-USA



