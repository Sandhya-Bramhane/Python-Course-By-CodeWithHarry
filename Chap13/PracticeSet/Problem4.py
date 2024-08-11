'''4. Write a program to filter a list of numbers which are divisible by 5'''

def divisible5(n):
  if(n%5 == 0):
    return True
  return False

a = [1,2,333324,4454,656,76768787,87,989898,77,5,55,11555]

f = list(filter(divisible5,a))
print(f)