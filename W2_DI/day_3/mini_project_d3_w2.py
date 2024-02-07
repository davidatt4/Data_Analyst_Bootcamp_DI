class Character:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10
        print(f"{self.name} is created with {self.life} life and {self.attack} attack.")

    def basic_attack(self, other_char):
        other_char.life -= self.attack
        print(f"{self.name} attacks {other_char.name}. {other_char.name}'s life is now {other_char.life}.")

class Druid(Character):
    def __init__(self, name):
        super().__init__(name)

    def meditate(self):
        self.life += 10
        self.attack -= 2
        print(f"{self.name} meditates. Life increased to {self.life}, attack decreased to {self.attack}.")

    def animal_help(self):
        self.attack += 5
        print(f"{self.name} gets help from animals. Attack increased to {self.attack}.")

    def fight(self, other_char):
        damage = 0.75 * self.life + 0.75 * self.attack
        other_char.life -= damage
        print(f"{self.name} fights {other_char.name}. {other_char.name}'s life is now {other_char.life}.")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)

    def brawl(self, other_char):
        damage = 2 * self.attack
        self.life += 0.5 * self.attack
        other_char.life -= damage
        print(f"{self.name} brawls with {other_char.name}. {self.name}'s life is now {self.life}, {other_char.name}'s life is now {other_char.life}.")

    def train(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} trains. Life increased to {self.life}, attack increased to {self.attack}.")

    def roar(self, other_char):
        other_char.attack -= 3
        print(f"{self.name} roars at {other_char.name}. {other_char.name}'s attack is now {other_char.attack}.")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name)

    def curse(self, other_char):
        other_char.attack -= 2
        print(f"{self.name} curses {other_char.name}. {other_char.name}'s attack is now {other_char.attack}.")

    def summon(self):
        self.attack += 3
        print(f"{self.name} summons power. Attack increased to {self.attack}.")

    def cast_spell(self, other_char):
        damage = self.attack / 5
        other_char.life -= damage
        print(f"{self.name} casts a spell on {other_char.name}. {other_char.name}'s life is now {other_char.life}.")


druid = Druid("Druid")
warrior = Warrior("Warrior")
mage = Mage("Mage")

druid.meditate()
druid.basic_attack(warrior)
druid.animal_help()
druid.fight(mage)


warrior.brawl(mage)
warrior.train()
warrior.roar(druid)


mage.curse(warrior)
mage.summon()
mage.cast_spell(druid)
