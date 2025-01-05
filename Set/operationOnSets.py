
fruits = {"apple", "cherry", "banana"}

popped_fruit = fruits.pop()     # Removes and returns an arbitrary element.
print(fruits)                   # Output: {'cherry', 'banana'}  - Arbitrary element
print(popped_fruit)             # Output: apple                 - Arbitrary element

fruits.clear()                  # Removes all elements.
print(fruits)                   # Output: set()


'''

fruits.remove("banana") # Remove a element
print(fruits)           # Output: {'apple', 'cherry'}

fruits.remove("blueberry")  # Try to remove a element which is not present
print(fruits)                # KeyError: 'blueberry'

fruits.discard("blueberry")  # Try to remove a element which is not present
print(fruits)                # Output: {'apple', 'cherry'}

fruits.discard("apple")  # Try to remove a element which is not present
print(fruits)                # Output: {'cherry'}


fruits.add("mango")     # Add a new element
print(fruits)           # Output: {'cherry', 'apple', 'banana', 'mango'}

fruits.add("apple")     # Try to add a duplicate
print(fruits)           # Output: {'cherry', 'apple', 'banana', 'mango'}

fruits.update(["mango", "grapes"])  # Add multiple elements
print(fruits)           # Output: {'grapes', 'apple', 'cherry', 'mango', 'banana'}

'''