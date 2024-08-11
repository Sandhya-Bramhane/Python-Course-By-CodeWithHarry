f = open("file.txt")

print(f.read())

f.close()


# the same can be written usig 'with' statement like this, so we don't need to close file:

with open("file.txt") as f:
    
    print(f.read())

