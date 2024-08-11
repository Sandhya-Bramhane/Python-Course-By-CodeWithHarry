'''7. Write a program to find out the line number where python is present from ques 6.'''



with open("log.txt") as f:
  lines = f.readlines()

lineno = 1

for line in lines:
  if("Python" in line):
    print(f"Yes python is present in this no: {lineno}")
    break
  lineno = lineno + 1

else:
     print(f"Python is not present in this {lineno}")

  
    