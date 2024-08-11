marks = {
  "sandhya": 84,
  "Divya": 94,
  "Aishwarya": 100,
}

# marks items show
print(marks.items())

# marks keys will show
print(marks.keys())

# marks values will show
print(marks.values())

# update to dictionary
marks.update({"Sandhya": 93 , "Bramhane": 32})
print(marks)

# what is store in the key
print(marks.get("Sandhya"))

# What is diffrence between this
print(marks.get("Sandhya2")) #its print 'None'

# print(marks["sandhya2"]) #its print 'error'

marks.clear()
print(marks)