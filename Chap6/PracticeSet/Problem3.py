'''3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams'''

c1 = "make a lot money"
c2 = "buy now"
c3 = "click this"
c4 = "subscribe this"



message = input("Enetr the comment : ")

if((c1 in message) or (c2 in message) or (c3 in message) or (c4 in message)):
  print(" This Comment is spam")

else:
  print("Nice Comment ♥")
