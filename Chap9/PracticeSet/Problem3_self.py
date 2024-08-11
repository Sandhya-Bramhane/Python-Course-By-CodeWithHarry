


def createTable(n):
  table2 = ""
  for i in range(1,11):
    table2 = table2 + f"{n} X {i} = {n*i}\n"

  with open(f"table2/table2_{n}", "w") as f:
    f.write(table2)

for i in range(2,21):
  createTable(i)
