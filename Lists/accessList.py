'''
# Indexing
my_list = [10, 20, 30, 40]
print(my_list[0])   # Output: 10
print(my_list[2])   # Output: 30
print(my_list[4])   # Error


# Negative Indexing
my_list = [10, 20, 30, 40]
print(my_list[-0])   # Output: 10
print(my_list[-2])   # Output: 30
print(my_list[-3])   # Output: 20
print(my_list[-4])   # Output: 10
print(my_list[-5])   # Error



# Slicing
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])     # Output: [20, 30, 40] (elements from index 1 up to, but not including, index 4)
print(my_list[:3])      # Output: [10, 20, 30] (elements from the beginning up to index 3)
print(my_list[2:])      # Output: [30, 40, 50] (elements from index 2 to the end)
print(my_list[:])       # Output: [10, 20, 30, 40, 50] (a copy of the entire list)



# Slicing with step
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4:2])       # Output: [20, 40] 
print(my_list[:3:-1])       # Output: [50]
print(my_list[2::2])        # Output: [30, 50]
print(my_list[::2])         # Output: [10, 30, 50]
print(my_list[::-1])        # Output: [50, 40, 30, 20, 10] Reversing the list

'''

# Slicing with negative index
my_list = [10, 20, 30, 40, 50]
# print(my_list[1:-3])        # Output: [20]
# print(my_list[-1:-5])       # Output: []
# print(my_list[-1:])         # Output: [50]
# print(my_list[-1:-5:1])     # Output: [] 
# print(my_list[-1:-6:-1])    # Output: [50, 40, 30, 20, 10]

print(my_list.index(20))