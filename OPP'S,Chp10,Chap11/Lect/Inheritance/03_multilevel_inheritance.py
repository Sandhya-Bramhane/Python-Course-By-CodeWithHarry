class Employee:
  a = 1

class Programmer(Employee):
  b = 2

class Manager(Programmer):
  c = 3


obj = Employee()

print(obj.a) #oprints the attribute
# print(obj.b) #Showing an error thier is no b attribute in employee class

obj = Programmer()
print(obj.a, obj.b)


obj = Manager()
print(obj.a, obj.b, obj.c)