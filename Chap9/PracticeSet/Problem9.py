'''Write a program to find out whether a file is identical & matches the content of 
another file.'''



with open("file.txt", "r") as f:
    content1 = f.read()

with open("poems.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Both files are matching")

else:
    print("No this Both files are not matching")




with open("this.txt", "r") as f:
    content3 = f.read()

with open("this_copy.txt", "r") as f:
    content4 = f.read()

if(content3 == content4):
    print("Both files are matching")

else:
    print("No this Both files are not matching")