def myfun():
  print("Hello world!")

myfun()
print(__name__)



def myfunsecond():
  print("Hello world!")


# this basically that this code will not exicute , bcoz we give directly adress to that this only will run only in this present file, this concept basicaaly use for send only we want functions data will be show thier

if __name__ == "__main__":
  #  if this code is directly exceuted by running the file its present in
  print("we are directly running code")
  myfunsecond()
  print(__name__)
