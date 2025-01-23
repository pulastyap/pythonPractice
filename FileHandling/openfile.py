
with open("/Users/pulastya/Downloads/test.txt") as file:
    lines = file.readlines()
    print(lines)




file = open("/Users/pulastya/Downloads/test.txt", "r")

full_content = file.read()
first_line = file.readline()

print(full_content)
print(first_line)

file.close()



