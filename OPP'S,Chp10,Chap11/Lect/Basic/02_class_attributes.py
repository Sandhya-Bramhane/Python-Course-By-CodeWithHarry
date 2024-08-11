
class Home:
    rooms = 5
    members = 6
    Owner = "Ramkrushna Bramhane"

Data1 = Home()
print(Data1.rooms, Data1.Owner)


Data2 = Home()
Data2.name = "SumanAai" # This is an instance attribute
print(Data2.Owner, Data2.rooms,Data2.name)

# Here name is instance attribute and slary and language are class attribute as they belong to the class
