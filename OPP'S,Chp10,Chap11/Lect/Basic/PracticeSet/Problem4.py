'''4. Add a static method in problem 2, to greet the user with hello.'''


class Calculator:
  def __init__(self, n):
    self.n = n

  def Calculation(self):
    print(f"The Squeare is : {self.n* self.n}")
    print(f"The Cube is : {self.n* self.n * self.n}")
    print(f"The Squareroot is : {self.n**1/2}")

  @staticmethod
  def greet():
    print("Hello User!")
   
a = Calculator(4)
a.Calculation()
a.greet()


