a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if(b ==0):
  raise ValueError("Hey our program is not meant to divide numbers by zero")

else:
  print(f"The division a/b is {a/b}")
