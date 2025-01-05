
wild_animals = {'Lion', 'Tiger', 'Buffalo', 'Elephant'}
pet_wild_animals = {'Buffalo', 'Elephant'}

wild_animals_tuple = ('Lion', 'Tiger', 'Buffalo', 'Elephant')
pet_wild_animals_tuple = ('Buffalo', 'Elephant')

print('Lion' in wild_animals)           # Output: True
print('Lion' in pet_wild_animals)       # Output: False

print(pet_wild_animals.issubset(wild_animals))      # Output: True
print(wild_animals.issuperset(pet_wild_animals))    # Output: True

print(wild_animals.issubset(pet_wild_animals))      # Output: False
print(pet_wild_animals.issuperset(wild_animals))    # Output: False

# Parameter can be any iterable
print(pet_wild_animals.issubset(wild_animals_tuple))      # Output: True
print(wild_animals.issuperset(pet_wild_animals_tuple))    # Output: True

print(pet_wild_animals <= wild_animals)      # Output: True
print(wild_animals >= pet_wild_animals)      # Output: True

print(wild_animals <= pet_wild_animals)      # Output: False
print(pet_wild_animals >= wild_animals)      # Output: False

print(pet_wild_animals <= wild_animals_tuple)      # Output: TypeError: '<=' not supported between instances of 'set' and 'tuple'
print(wild_animals >= pet_wild_animals_tuple)      # Output: TypeError: '>=' not supported between instances of 'set' and 'tuple'

