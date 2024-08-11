# ==========This only use to show that this is which type of the data you have stored===========


# its not neccesary to do
n : int = 5

name: str = "Sandhya"


# int function how this work

def sum(a: int,b: int) -> int:
  return a + b

print(sum(3,23))


# advance type hints
from typing import List,Union, Dict,Tuple

# __List of integers
numbers: List[int] = [1,2,3,4,5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("ALice",30)

# Dictionary with string keys and integer values
scores : Dict[str,int] = {"ALice":90, "Bob": 86}

# Union type for variables that can hold multiple types
identifier: Union[int,str] = "ID123"
identifier = 12345 #Also valid

