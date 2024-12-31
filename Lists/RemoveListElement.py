
fav_animals = ['Dog', 'Lion', 'Cat', 'Cow', 'Tiger', 'Goat', 'Buffalo', 'Lion', 'Cow']

fav_animals.pop(-3)     
print(fav_animals)   

'''
# Delete all elements of list
fav_animals.clear() 
print(fav_animals)                          # Output: []



# Delete single element
del fav_animals[2]                          # Delete Cat and removes from list
print(fav_animals)                          # Output: ['Dog', 'Lion', 'Cow', 'Tiger', 'Goat', 'Buffalo', 'Lion', 'Cow']

# Delete sliced list
del fav_animals[3:6]                        # Delete element at index 3 to 5
print(fav_animals)                          # Output: ['Dog', 'Lion', 'Cow', 'Lion', 'Cow']

del fav_animals[::2]                        # Delete element at index 1, 3 and 5
print(fav_animals)                          # Output: ['Lion', 'Lion']

del fav_animals                             # Delete entire list
print(fav_animals)                          # NameError: name 'fav_animals' is not defined



# Removes last element if index not given
popped_animal = fav_animals.pop()           # Cow will be assigned to popped animal
print(fav_animals)                          # Output: ['Dog', 'Lion', 'Cat', 'Cow', 'Tiger', 'Goat', 'Buffalo', 'Lion']
print(popped_animal)                        # Output: Cow

# Removes element at given index
pos_popped_animal = fav_animals.pop(2)      # Cat will be assigned to pos_popped_animal
print(fav_animals)                          # Output: ['Dog', 'Lion', 'Cow', 'Tiger', 'Goat', 'Buffalo', 'Lion']
print(pos_popped_animal)                    # Output: Cat

# Removes element at given index
neg_popped_animal = fav_animals.pop(-3)     # Goat will be assigned to neg_popped_animal
print(fav_animals)                          # Output: ['Dog', 'Lion', 'Cow', 'Tiger', 'Buffalo', 'Lion']
print(neg_popped_animal)                    # Output: Goat

# Error if index is out of range
neg_popped_animal = fav_animals.pop(10)     # IndexError: pop index out of range




# Removes the first occurrence of a specific value.
fav_animals.remove('Lion')
print(fav_animals)          # Output: ['Dog', 'Cat', 'Cow', 'Tiger', 'Goat', 'Buffalo', 'Lion', 'Cow']

# Try to remove an element which is not present
fav_animals.remove('Leopard')
print(fav_animals)          # ValueError: list.remove(x): x not in list

'''