'''2. Write a class “Calculator” capable of finding square, cube and square root of a 
number.'''


class Calculator:
  def __init__(self, n):
    self.n = n

  def Calculation(self):
    print(f"The Squeare is : {self.n* self.n}")
    print(f"The Cube is : {self.n* self.n * self.n}")
    print(f"The Squareroot is : {self.n**1/2}")
   
a = Calculator(4)
a.Calculation()