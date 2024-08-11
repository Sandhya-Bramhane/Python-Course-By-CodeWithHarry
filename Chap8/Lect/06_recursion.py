# suppose we give example of factorial to undstand the recursion in easy form

# we know factorial we can writ this like n * fun(n-1)

def factorial(n):
  if(n==1 or n==0):
    return 1
  return n * factorial(n-1)

n = int(input("Enter a Number: "))

print(f"The factorial of number is: {factorial(n)}")