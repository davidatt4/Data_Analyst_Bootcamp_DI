#1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1=Cat('Daisy',5)
cat2=Cat('Belle',7)
cat3=Cat('Maria',2)
def oldest_age(*args):
    return max(args)
print(f'The oldest cat is {cat2.name} and is {oldest_age(cat1.age,cat2.age,cat3.age)}')

#2
class Dog:
    def __init__(self,dog_name,dog_height):
        self.name=dog_name
        self.height=dog_height
    def bark(self):
        print('{} goes woof!'.format(self.name))
    def jump(self):
        jump_height=self.height*2
        print(f'{self.name} jumps {jump_height}cm high!')
davids_dog=Dog('Rex',50)
print(f'Dog name:{davids_dog.name}')
print(f'Dog height:{davids_dog.height} cm')

davids_dog.bark()
davids_dog.jump()

sarahs_dog=Dog('Teacup',20)
print(f'Dog name:{sarahs_dog.name}')
print(f'Dog height:{sarahs_dog.height} cm')

sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height>sarahs_dog.height:
    print(f'The bigger dog is {davids_dog.name}')
elif davids_dog.height<sarahs_dog.height:
    print(f'The bigger dog is {sarahs_dog.name}')
else:
    print('Both dogs are the same height')

#3
class Song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway=Song(["There's a lady who's sure",
                 "all the glitters is gold",
                 "and she's buying a stairway to heaven"
 ])
stairway.sing_me_a_song()

#4
class Zoo:
    def __init__(self,zoo_name):
        self.name=zoo_name
        self.animals=[]
    def add_animals(self,new_animal):
        if new_animal not in self.animals:
            print(f"{new_animal} has been added to the zoo")
    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)
    def sell_animals(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold")
    def sort_animals(self):
        self.animals.sort()
        print("Animals in the zoo(Sorted):")
        for animal in self.animals:
            print(animal)
    
    def get_groups(self):
        animal_groups={}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in animal_groups:
                animal_groups[first_letter] = [animal]
            else:
                animal_groups[first_letter].append(animal)

        print("Animal Groups:")
        for letter, group in animal_groups.items():
            print(f"Group {letter}: {', '.join(group)}")
ramat_gan_safari = Zoo(zoo_name="Ramat Gan Safari")

ramat_gan_safari.add_animals("Elephant")
ramat_gan_safari.add_animals("Baobab")
ramat_gan_safari.add_animals("Tiger")
ramat_gan_safari.add_animals("Lion")
ramat_gan_safari.add_animals("Giraffe")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animals("Lion")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
ramat_gan_safari.sort_animals()
