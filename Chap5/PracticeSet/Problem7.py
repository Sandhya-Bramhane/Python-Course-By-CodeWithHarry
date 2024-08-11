'''7. If the names of 2 friends are same; what will happen to the program in problem 
6?'''

'''6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique.'''

Langdict = {}

Name = input("Eneter your name: ")
Language = input("Enter you fav language: ")

Langdict.update({Name:Language})

Name = input("Eneter your name: ")
Language = input("Enter you fav language: ")

Langdict.update({Name:Language})

Name = input("Eneter your name: ")
Language = input("Enter you fav language: ")

Langdict.update({Name:Language})

Name = input("Eneter your name: ")
Language = input("Enter you fav language: ")

Langdict.update({Name:Language})

print(Langdict)


# Last enter same name is printend not first included