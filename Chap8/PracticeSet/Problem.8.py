'''8. Write a python function to print multiplication table of a given number '''





def multiplicationTable(n):
  for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

n = int(input("Enter the number: "))

multiplicationTable(n)

