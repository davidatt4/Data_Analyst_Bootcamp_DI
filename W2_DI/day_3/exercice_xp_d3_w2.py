#1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.amount} {self.currency}s'

    def __add__(self, other):
        if isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')
        elif isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        else:
            return Currency(self.currency, self.amount + other.amount)

    def __iadd__(self, other):
        if isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            self.amount += other.amount
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  
print(int(c1))  
print(repr(c1))  
print(c1 + 5)   
print(c1 + c2)  
print(c1)       
c1 += 5
print(c1)       
c1 += c2
print(c1)       
#3
import string
import random

length=5
characters=string.ascii_letters
random_string=''.join(random.choice(characters)for i in range(length))
print(random_string)
#4
from datetime import date
today=date.today()
print(today)
#5
from datetime import date
today=date.today()
d0=today
d1=date(2024,1,1)
amount_time=d1-d0
print(f'It remains {amount_time} until January 1st')
#6
from datetime import datetime

def minutes_lived(birthdate):
    birthdate_obj = datetime.strptime(birthdate, '%Y-%m-%d')
    current_datetime = datetime.now()
    
    
    time_lived = current_datetime - birthdate_obj
    minutes_lived = int(time_lived.total_seconds() / 60)
    
    
    print(f"You have lived for {minutes_lived} minutes.")


birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
minutes_lived(birthdate_input)
#7
from faker import Faker
fake=Faker
users=[]
def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)
    for _ in range(5):
        add_user()
for idx, user in enumerate(users, start=1):
    print(f"User {idx}:")
    print(f"Name: {user['name']}")
    print(f"Address: {user['address']}")
    print(f"Language Code: {user['language_code']}")
    print("\n")