import os
import shutil as sh

with open("/Users/pulastya/Desktop/test2.txt", "w") as file:
    file.write("I am Pulastya.\nI love Python")

sh.copy("/Users/pulastya/Desktop/test2.txt", "/Users/pulastya/Desktop/test.txt")