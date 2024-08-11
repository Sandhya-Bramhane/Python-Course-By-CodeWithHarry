# 2. Write a python program using function to convert fahrenheit to celsius.

# first we will undtsand how is fahrenheit to celsius
# c = 5*(f-32)/9


def f_to_c(f): 
   return 5*(f-32)/9

f = int(input("Enter temprature in F: "))

c = f_to_c(f)

print(f"{round(c,2)} degree C")