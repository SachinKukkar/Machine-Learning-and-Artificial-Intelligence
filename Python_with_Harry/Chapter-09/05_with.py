# The file can be read using the following statement , so we need not to use f.close()

with open("file.txt") as f:
    print(f.read())