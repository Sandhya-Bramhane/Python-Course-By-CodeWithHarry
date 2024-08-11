a = int(input("Enter your age: "))

if(a>=18): # in this after enter we get some tab minimun space is nothing but in python is indented
  print("You are above the age of consent")
  print("Good for you")

elif(a < 0):
  print("You are entering invalid age")

else:
  print("You are below the age of consent")

print("End of Program")