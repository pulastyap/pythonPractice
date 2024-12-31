text = "This is a test string."
words = text.rsplit()                # Split by whitespace
print(words)                         # Output: ['This', 'is', 'a', 'test', 'string.']

data = "apple,banana,orange,grape"
fruits = data.rsplit(",")            # Split by comma
print(fruits)                        # Output: ['apple', 'banana', 'orange', 'grape']

path = "/home/user/documents/file.txt"
parts = path.rsplit("/")                # Split by forward slash
print(parts)                            # Output: ['', 'home', 'user', 'documents', 'file.txt']

parts = text.rsplit(" ", 2)             # Use of maxsplit
print(parts)                            # Output: ['This is a', 'test', 'string.']

# Split an empty string
empty_string = ""
result = empty_string.rsplit()
print(result)                           # Output: [] (an empty list)

empty_string2 = "   "                   # String containing only spaces
result2 = empty_string2.rsplit()
print(result2)                          # Output: [] (an empty list)

