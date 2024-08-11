# 1. Write a program using functions to find greatest of three numbers.



def greatest(n1,n2,n3):

  if(n1 > n2 and n1 > n3):
    return n1
  
  elif(n2 > n1 and n2 > n3):
    return n2
  
  else:
    return n3
  

n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
n3 = int(input("Enter the number: "))


print(greatest(n1,n2,n3))
