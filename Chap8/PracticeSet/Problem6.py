# 6. Write a python function which converts inches to cms.

def inch_to_cm(inch):
  return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The corresponding value in cm is: {inch_to_cm(n)}")