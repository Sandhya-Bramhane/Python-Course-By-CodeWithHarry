try:
  a = int(input("Enter The number : "))
  print(a)

except ValueError as v:
  print("Heyyy")
  print(v)
except Exception as e:
  print(e)

print("Please enter the valid data type value")