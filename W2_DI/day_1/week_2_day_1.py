class Dog():
    print('an object was created')
    self.name=name
       self.color=color
        self.height=height
        self.favorite_toys=favorite_toys
    
    
    def bark(self):
        print(f'{self.name} barks!WAF')
    def walk(self,distance:int):
        print(f'{self.name}walks{distance}km')
    def rename(self,new_name):
        self.name=new_name
        return self.name


#dianas_dog=Dog('Lieto','Black')
#dianas_dog_name='Lieto'
#print(dianas_dog_name)

alex_dog=Dog('Rex','Beige',80,['ball','mouse','shoe'])
print(alex_dog.name,alex_dog.color)
alex_dog.favorite_toys.append('rope')
print(alex_dog.__dict__)

#New example
class BankAccount():
    def __init__(self, account_number, balance=0)->None:
        self.account_number=account_number
        self.balance=balance
        self.transactions=[]

def view_balance(self):
    print(f'Balance for {self.account_number} is ${self.balance}')
    self.transactions.append('withdraw')

def deposit(self,dep_amount):
    if dep_amount<=0:
        print('invalid amount')
    elif amount<50:
        print('minimal deposit is 100')
    else:
        self.balance+=dep_amount
        self.view_balance()
        self.transactions.append('deposit')
   
def withdraw(self,w_amount):
    if w_amount>self.balance:
        print('insufficient amount')
    else:
        self.balance-=w_amount
def view_transactions(self):
    print('\n'.join(self.transactions))

account1=BankAccount(1234567,500)
account1.view_balance()
account1.deposit(300)
account1.view_balance()
account1.withdraw(100)
account1.view_balance()
account1.view_transactions()
