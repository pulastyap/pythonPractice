file = open("/Users/pulastya/Downloads/test.txt", "a")

tot_chars = file.write("I am Pulastya Pandey\nI love Python\nI make videos on Python programming")
print(tot_chars)

file.writelines(["Pulastya", "Pandey\n", "I am living in Chicago"])
print(file.readable())
print(file.writable())

file.close()
