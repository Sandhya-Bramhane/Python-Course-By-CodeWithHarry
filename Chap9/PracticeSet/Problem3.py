'''3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old'''

def generateTable(n):
  table = ""
  for i in range(1,11):
    table += f"{n} X {i}= {n*i}\n"

  with open(f"table/table_{n}","w") as f:
    f.write(table)


for i in range(2,21):
  generateTable(i)



'''Summary
Define a function to create a multiplication table.
Use a loop to generate each line of the table.
Write the table to a file.
Call the function for each number from 2 to 20.'''


'''This will create files table_2, table_3, ..., table_20 in a folder named table, each containing the multiplication table for the corresponding number.'''

'''Function: A block of code designed to perform a specific task.
String: A sequence of characters, like "Hello" or "2 X 1 = 2".
For Loop: A way to repeat a block of code multiple times.
File Handling: Opening a file, writing to it, and then closing it.'''