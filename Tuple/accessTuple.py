
# Indexing
my_tuple = (10, 20, 30, 40)
print(my_tuple[0])   # Output: 10
print(my_tuple[2])   # Output: 30
print(my_tuple[4])   # IndexError: tuple index out of range





# Negative Indexing
my_tuple = (10, 20, 30, 40)
print(my_tuple[-0])   # Output: 10
print(my_tuple[-2])   # Output: 30
print(my_tuple[-3])   # Output: 20
print(my_tuple[-4])   # Output: 10
print(my_tuple[-5])   # IndexError: tuple index out of range


# Slicing
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])     # Output: (20, 30, 40) 
print(my_tuple[:3])      # Output: (10, 20, 30)
print(my_tuple[2:])      # Output: (30, 40, 50)
print(my_tuple[:])       # Output: (10, 20, 30, 40, 50)

# Slicing with step
print(my_tuple[1:4:2])       # Output: (20, 40)
print(my_tuple[:3:-1])       # Output: (50,)
print(my_tuple[2::2])        # Output: (30, 50)
print(my_tuple[::2])         # Output: (10, 30, 50)
print(my_tuple[::-1])        # Output: (50, 40, 30, 20, 10)

# Slicing with negative index
print(my_tuple[1:-3])        # Output: (20,)
print(my_tuple[-1:-5])       # Output: ()
print(my_tuple[-1:])         # Output: (50,)
print(my_tuple[-1:-5:1])     # Output: () 
print(my_tuple[-1:-6:-1])    # Output: (50, 40, 30, 20, 10)

