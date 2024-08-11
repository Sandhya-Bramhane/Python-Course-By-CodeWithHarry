class Employee:
  def __init__(self):
    print("Constructer Of Employee")
  a = 1

class Programmer(Employee):
  def __init__(self):
    print("Constructer Of Programmer")
  b = 2

class Manager(Programmer):
  def __init__(self):
    super().__init__()
    print("Constructer Of Manager")
  c = 3


# obj = Employee()

# print(obj.a) 

# obj = Programmer()
# print(obj.a, obj.b)


obj = Manager()
print(obj.a, obj.b, obj.c)