
fav_animals = ['Dog', 'Lion', 'Cat', 'Cow', 'Tiger', 'Goat', 'Buffalo']

# Change an element using index
fav_animals[2] = "Rabit"
print(fav_animals)          # Output: ['Dog', 'Lion', 'Rabit', 'Cow', 'Tiger', 'Goat', 'Buffalo']

# Change an element using negative index
fav_animals[-1] = "Squirrel"
print(fav_animals)          # Output: ['Dog', 'Lion', 'Rabit', 'Cow', 'Tiger', 'Goat', 'Squirrel']

# Change an element using slicing
fav_animals[2:5] = ["Buffalo", "Cat", "Rat"]
print(fav_animals)          # Output: ['Dog', 'Lion', 'Buffalo', 'Cat', 'Rat', 'Goat', 'Squirrel']

fav_animals[1:4] = ["Cow"]
print(fav_animals)          # Output: ['Dog', 'Cow', 'Rat', 'Goat', 'Squirrel']

