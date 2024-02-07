class Farm:
    def __init__(self,farm_name):
        self.farm_name = farm_name
        self.animals={}
    def add_animal(self,animal,quantity=1):
        if animal in self.animals:
            self.animals[animal]+=quantity
        else:
            self.animals[animal]=quantity

    def get_info(self):
        farm_info=f"{self.farm_name}'s farm\n"
        for animal,quantity in self.animals.items():
            farm_info+=f"{animal}:{quantity}\n"

            farm_info="E-I-E-I-O"
            return farm_info
    def get_animal_types(self):
        return sorted(list(self.animals.keys()))
    def get_short_info(self):
        animal_types=self.get_animal_types()
        animal_str=','.join(animal_types)
        return f"{self.farm_name}'s farm has {animal_str}."

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_short_info())
print("{:<15} {:<5}".format("Animal", "Quantity"))
for animal_type, quantity in macdonald.animals.items():
    print("{:<15} {:<5}".format(animal_type, quantity))
animal_types = macdonald.get_animal_types()
print("Animal types:", animal_types)

short_info = macdonald.get_short_info()
print(short_info)