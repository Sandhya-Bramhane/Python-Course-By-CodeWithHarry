'''3. Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?'''

class Change:
  a = 23


object = Change()
print(object.a) # printing the class attribute because we not created instance attribute


# now we created instance attribute due to class attribute is not printing
object.a = 0
print(object.a)


# answer is No , class attribute is not changed, we only made a new instance sttribute 

# We can Print our attribute this like you know

print(Change.a)