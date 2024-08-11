'''6. Write a program to calculate the grade of a student from his marks from the 
following scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => F'''

marks = int(input("Enetr the marks and take the grade: "))

if(marks >= 90 and marks <= 100):
  print("Ex")

elif(marks < 90 and marks >= 80):
  print("A")

elif(marks >= 70 and marks < 80):
  print("B")

elif(marks >= 60 and marks < 70):
  print("C")

elif(marks >= 50 and marks < 60):
  print("D")

else:
  print("F")

