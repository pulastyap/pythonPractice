
fav_animals = ['Dog', 'Cow', 'Cat']

fav_animals_tuple = tuple(fav_animals)

print(fav_animals)                  # Output: ['Dog', 'Cow', 'Cat']
print(fav_animals_tuple)            # Output: ('Dog', 'Cow', 'Cat')
print(tuple(range(4)))              # Output: (0, 1, 2, 3)


'''
my_tuple = (1, 2, 3, "apple", 3.14)
empty_tuple = ()            # An empty tuple
single_item_tuple = (5,)    # Important: a trailing comma is needed for single-item tuples
single_item_tuple1 = (5)    # Important: This will be considered as int but not tuple
my_tuple1 = 1, 2, 3         # Tuple without parentheses

print(my_tuple)                         # Output: (1, 2, 3, 'apple', 3.14)
print(empty_tuple)                      # Output: ()
print(single_item_tuple)                # Output: (5,)
print(single_item_tuple1)               # Output: 5
print(my_tuple1)                        # Output: (1, 2, 3)

print(type(single_item_tuple))          # Output: <class 'tuple'>
print(type(single_item_tuple1))         # Output: <class 'int'>
print(type(empty_tuple))                # Output: <class 'tuple'>
print(type(my_tuple))                   # Output: <class 'tuple'>
print(type(my_tuple1))                  # Output: <class 'tuple'>
'''
