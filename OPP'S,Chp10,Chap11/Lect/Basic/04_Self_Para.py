class Home:
    rooms = 5
    name = "Ramai" #this is class attribute
    members = 6
    Owner = "Ramkrushna Bramhane"

    #you can add function in the class

    def getInfo(self):
        print(f"In Home Rooms is : {self.rooms}. and the owner of is : {self.Owner}")

        #self parameter is necessary
        #self is convention

Data = Home()
Data.name = "SumanAai" # This is an instance attribute

Data.getInfo()
# Home.getInfo(Data)