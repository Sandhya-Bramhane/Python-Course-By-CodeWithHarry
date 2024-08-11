'''2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
‘Pets’. Add a method ‘bark’ to class ‘Dog’.'''


class Animal:
  def dog():
    pass


class Pets(Animal):
  pass

class Dog(Pets):
  @staticmethod
  def bark():
    print("Bhow Bhow__")
  

d = Dog()
d.bark()