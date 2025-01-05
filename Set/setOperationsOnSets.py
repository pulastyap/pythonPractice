
wild_animals = {'Lion', 'Tiger', 'Buffalo', 'Elephant'}
pet_animals = {'Cow', 'Buffalo', 'Elephant', 'Dog'}

pet_and_wild_animals = wild_animals | pet_animals
print(pet_and_wild_animals)     # Output: {'Cow', 'Dog', 'Tiger', 'Buffalo', 'Elephant', 'Lion'}

pet_wild_animals = wild_animals & pet_animals
print(pet_wild_animals)         # Output: {'Buffalo', 'Elephant'}

pet_but_not_wild_animals = pet_animals - wild_animals
print(pet_but_not_wild_animals)       # Output: {'Cow', 'Dog'}

pet_or_wild_but_not_both = pet_animals ^ wild_animals
print(pet_or_wild_but_not_both)       # Output: {'Lion', 'Dog', 'Tiger', 'Cow'}

# Multiple operations together
my_animals = (pet_animals ^ wild_animals) - pet_animals
print(my_animals)



