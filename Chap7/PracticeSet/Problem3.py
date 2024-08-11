# Attempt problem 1 using while loop.


# 1. Write a program to print multiplication table of a given number using for loop.

number = int(input("Enter the number: "))

counter = 1

while counter <= 10:
  result = counter * number
  print(result)
  counter +=1