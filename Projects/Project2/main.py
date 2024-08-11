import random

n = random.randint(1,100)
a = -1
guesses = 1

while(a != n):
   
   a = int(input("Guess the number ? "))

   if(a > n):
      print("Lower number please __")
      guesses = guesses + 1
   elif(a < n):
      print("Higher Number please")
      guesses = guesses + 1

print(f"You have guessed the number {n} correctly in {guesses} attempt")