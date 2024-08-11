# list container to store any data values
# list is mutable
friends = ["apple","2",False,33.83, "divya" , "yash"]

friends.append("sandhya")

print(friends)

friends = ["Tomato","2",False,33.81, "divya" , "yash", "sandhya"]

print(friends)

l1 = [1,3,5,6]

l1.sort()
print(l1)

l1.insert(2, 3453345) # we can directly insert in this at any position by this (index,data)
print(l1)

l1.pop(3)
print(l1)

l1.reverse()
print(l1)

l1.remove(6)
print(l1)