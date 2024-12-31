
fav_wild_animals = ('Lion', 'Tiger', 'Elephant', 'Lion')

print(fav_wild_animals.count('Lion'))                     # Output: 2
print(fav_wild_animals.count('Tiger'))                    # Output: 1
print(fav_wild_animals.count('Cow'))                      # Output: 0


print(fav_wild_animals.index('Lion'))                     # Output: 0
print(fav_wild_animals.index('Tiger'))                    # Output: 1
print(fav_wild_animals.index('Cow'))                      # ValueError: tuple.index(x): x not in tuple

