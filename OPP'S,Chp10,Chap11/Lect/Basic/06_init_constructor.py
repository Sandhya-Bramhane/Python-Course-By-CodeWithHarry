class Home:
    rooms = 44
    members = 6
    Owner = "Ramkrushna Bramhane"

    #init is special method we call it dunder method
    #dunder methos is atomatically is called
    def __init__(self, name, rooms, members, Owner):
        
        self.name = name
        self.rooms = rooms
        self.members = members
        self.Owner = Owner
        print("I am creating an object")



# Suppose i take argument here to directly print the values its happen due to the '__init__'

Data = Home("Sandhya",36 ,8 ,"Mangal Bramhane")

Data.name = "Sandhya"
print(Data.name, Data.rooms,Data.members,Data.Owner)


