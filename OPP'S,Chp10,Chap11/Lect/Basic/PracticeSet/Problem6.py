'''6. Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects'''

from random import randint

class Train:


  def __init__(slf, trainNo):
    slf.trainNo = trainNo


  def Book(slf, fro, to):
    print(f"Ticket is book in train No: {slf.trainNo} from {fro} to {to}")

  def getStatus(slf):
    print(f"Train {slf.trainNo} is running on time ")

  def getFare(slf,fro, to):
    print(f"Ticket Full info is train No: {slf.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12234)
t.Book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")