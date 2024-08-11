class Employee:
  company = "ITC"
  salary = 120000
  def show(self):
    print(f"The Company name is: {self.company} and the salary is is given by compnay is : {self.salary}")

class coder:
  language = "python"

  def printlanguages(self):
    print(f"Out of all the languages here is your language: {self.language}")




class Programmer(Employee, coder):
  company = "ITC Infotech"

  def showLanguage(self):
    print(f"The name of company is:  {self.company} and he is good with {self.language} language")



a = Employee()
b = Programmer()

b.show()
b.printlanguages()
b.showLanguage()
