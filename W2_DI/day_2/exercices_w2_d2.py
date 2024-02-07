#1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Siamese(Cat):
    def sing(self,sounds):
        return f'{sounds}'

bengal_cat = Bengal(name="BengalCat", age=3)
chartreux_cat = Chartreux(name="ChartreuxCat", age=2)
siamese_cat = Siamese(name="SiameseCat", age=4)

all_cats=[bengal_cat,chartreux_cat,siamese_cat]

sara_pets=Pets(animals=all_cats)

sara_pets.walk()

#2
class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def bark(self):
        return f'{self.name} is barking'
    def run_speed(self):
        return (self.weight/self.age*10)
    def fight(self, other_dog):
        self_speed = self.run_speed() * self.weight
        other_dog_speed = other_dog.run_speed() * other_dog.weight

        if self_speed > other_dog_speed:
            return f'{self.name} won the fight!'
        elif self_speed < other_dog_speed:
            return f'{other_dog.name} won the fight!'
        else:
            return 'It was a draw!'
    
dog1 = Dog(name='Rex', age=8, weight=23)
dog2 = Dog(name='Pit', age=5, weight=13)
dog3 = Dog(name='Doggy', age=9, weight=12)
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())
print(f'{dog1.name}\'s running speed: {dog1.run_speed()}')
print(f'{dog2.name}\'s running speed: {dog2.run_speed()}')
print(f'{dog3.name}\'s running speed: {dog3.run_speed()}')
result12 = dog1.fight(dog2)
result23 = dog2.fight(dog3)
result31 = dog3.fight(dog1)
print(result12)
print(result23)
print(result31)


#3
import random
class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def bark(self):
        return f'{self.name} is barking'
    def run_speed(self):
        return (self.weight/self.age*10)
    def fight(self, other_dog):
        self_speed = self.run_speed() * self.weight
        other_dog_speed = other_dog.run_speed() * other_dog.weight

        if self_speed > other_dog_speed:
            return f'{self.name} won the fight!'
        elif self_speed < other_dog_speed:
            return f'{other_dog.name} won the fight!'
        else:
            return 'It was a draw!'

import random
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        bark_output = self.bark()
        print(bark_output)
        self.trained = True

    def play(self, *dog_names):
        all_dogs = ', '.join(dog_names)
        print(f'{all_dogs} all play together')

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f'{self.name} does a barrel roll',
                f'{self.name} stands on his back legs',
                f'{self.name} shakes your hand',
                f'{self.name} plays dead'
            ]
            chosen_trick = random.choice(tricks)
            print(chosen_trick)
        else:
            print(f'{self.name} is not trained yet')


if __name__ == "__main__":
    pet_dog = PetDog(name='Buddy', age=2, weight=15)
    pet_dog.train()
    pet_dog.play('Max', 'Charlie')
    pet_dog.do_a_trick()
#4
class Family:
    def __init__(self,members,last_name):
        self.members=members
        self.last_name=last_name
    def born(self,**kwargs):
        self.members.append(kwargs)
        print(f'Congratulations!{kwargs['name']} has been born in {self.last_name} family')
    def is_18(self,member_name):
        for member in self.members:
            if member['name']==member_name:
                return member['age']>=18
        return False
    def family_presentation(self):
        print(f"Family Name:{self.last_name}")
        print("Family members")
        for member in self.members:
            print(f"Name: {member['name']},Age:{member['age']},Gender:{member['gender']}, is child:{member['is child']}")

family_members:[
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]
my_family = Family(last_name='Smith', members=family_members)
my_family.born(name='David', age=0, gender='Male', is_child=True)
is_over_18 = my_family.is_18(member_name='Michael')
print(f"Is Michael over 18? {is_over_18}")
my_family.family_presentation()

#5
class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def family_presentation(self):
        print(f"Here is our family {self.last_name}")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}")

    def born(self, name, age, gender, is_child):
        new_member = {'name': name, 'age': age, 'gender': gender, 'is_child': is_child}
        self.members.append(new_member)


class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, member_index):
        member = self.members[member_index]
        if member['age'] >= 18:
            print(f"{member['name']} can use the power: {member['power']}")
        else:
            raise Exception(f"{member['name']} is not over 18 years old.")

    def incredible_presentation(self):
        print(f"Here is our powerful family {self.last_name}")
        super().family_presentation()


incredibles_family = TheIncredibles('Incredibles', [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

incredibles_family.incredible_presentation()
incredibles_family.born('Baby Jack', 1, 'Male', True)
baby_jack_index = len(incredibles_family.members) - 1
incredibles_family.incredible_presentation()
try:
    incredibles_family.use_power(0)  
except Exception as e:
    print(f"Exception: {e}")
