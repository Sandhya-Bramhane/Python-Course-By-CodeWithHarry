'''2. Write a program to input name, marks and phone number of a student and format it
using the format function like below:
“The name of the student is Harry, his marks are 72 and phone number is 99999888”'''

name = input("Enter the Name: ")
marks = int(input("Enter Marks: "))
phone = int(input("Phone Number: "))

s = "The name of the student is {} ,her marks are {} and phone number is {}".format(name,marks,phone)

print(s)