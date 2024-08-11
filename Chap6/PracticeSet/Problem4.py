'''4. Write a program to find whether a given username contains less than 10 
characters or not.
'''
name = input("Enter the name: ")

if(len(name) < 10):
  print("Name contain leas than 10 charcters")

else:
  print("Name contain greater than 10 charcters")