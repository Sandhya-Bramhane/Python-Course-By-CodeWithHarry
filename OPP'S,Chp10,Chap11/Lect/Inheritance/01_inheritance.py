class Employee:
  company = "ITC"
  def show(self):
    print(f"The name is: {self.name} and the salary is: {self.salary}")


# This is wrong methos to copy data from class into the new class
# class Programmer:
#   company = "ITC Infotech"

  # def show(self):
  #   print(f"The name is {self.name} and the salary is {self.salary}")

  # def showlanguage(self):
  #   print(f"The name is {self.name} and he is good with {self.language} language")



# Use this approach
# inheritance class
class Programmer(Employee):
  company = "ITC Infotech"

  def showlanguage(self):
    print(f"The name is {self.name} and he is good with {self.language} language")



a = Employee()
b = Programmer()

print(a.company, b.company)