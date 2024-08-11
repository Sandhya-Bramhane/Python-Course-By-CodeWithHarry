'''1. Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle'''

f = open("poems.txt")

data = f.read()

if("twinkel" in data):
  print("twinkel is present in content")

else:
  print("twinkel is Not present")

f.close()
