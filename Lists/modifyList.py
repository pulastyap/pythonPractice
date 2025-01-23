
fav_animals = ["Dog", "Cat", "Cow", "Goat"]
cute_animals = ["Rabit", "Squirrel"]

print(fav_animals)

# Add an element at the end
fav_animals.append("Buffalo")       # ["Dog", "Cat", "Cow", "Goat", "Buffalo"]
print(fav_animals)                  # Output: ['Dog', 'Cat', 'Cow', 'Goat', 'Buffalo']

# Add an element at a specific position : You can use negative index as well
fav_animals.insert(-15, "Lion")       # ['Dog', 'Lion', 'Cat', 'Cow', 'Goat', 'Buffalo']
print(fav_animals)                  # Output: ['Dog', 'Lion', 'Cat', 'Cow', 'Goat', 'Buffalo']

# Add an element at a specific position using negative index
fav_animals.insert(-2, "Tiger")     # ['Dog', 'Lion', 'Cat', 'Cow', 'Tiger', 'Goat', 'Buffalo']
print(fav_animals)                  # Output: ['Dog', 'Lion', 'Cat', 'Cow', 'Tiger', 'Goat', 'Buffalo']

# Add elements from another list
fav_animals.extend(cute_animals)    # ['Dog', 'Lion', 'Cat', 'Cow', 'Tiger', 'Goat', 'Buffalo', 'Rabit', 'Squirrel']
print(fav_animals)                  # Output: ['Dog', 'Lion', 'Cat', 'Cow', 'Tiger', 'Goat', 'Buffalo', 'Rabit', 'Squirrel']

