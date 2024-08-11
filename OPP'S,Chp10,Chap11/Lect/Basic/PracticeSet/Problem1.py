'''Create a class “Programmer” for storing information of few programmers 
working at Microsoft.'''

class Programmer:
  company = "Microsoft"

  def __init__(self, name, salary, pin):
    self.name = name
    self.salary = salary
    self.pin = pin

p1 = Programmer("Sandhya Bramhane", 1200000, 4242)
print(p1.company,p1.name,p1.salary,p1.pin)

p2 = Programmer("Khushbu Patil", 1000000, 4242)
print(p2.company,p2.name,p2.salary,p2.pin)

p3 = Programmer("Prerna Patil", 1100000, 4242)
print(p3.company,p3.name,p3.salary,p3.pin)