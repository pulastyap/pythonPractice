
wild_animals = {'Lion', 'Tiger', 'Buffalo', 'Elephant'}
frozen_wild_animals = frozenset(wild_animals)

print(wild_animals)
print(frozen_wild_animals)

dict1 = {frozen_wild_animals: 1}    # Frozen set is hashable
print(dict1)


