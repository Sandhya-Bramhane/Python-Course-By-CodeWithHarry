'''5. Write a program to find the maximum of the numbers in a list using the reduce 
function.'''
from functools import reduce
l = [1,2,34,44,656,767,87,98,77,5,55,115]

def greater(a,b):
  if(a>b):
    return a
  return b

print(reduce(greater,l))