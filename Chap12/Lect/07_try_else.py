try:
  a = int(input("Enter The number : "))
  print(a)

except ValueError as v:
  print("Heyyy")
  print(v)
except Exception as e:
  print(e)

else:
  print("I am inside else")


# so when we use try with else , then when the try block code is excuted then atomatically else also will be excute