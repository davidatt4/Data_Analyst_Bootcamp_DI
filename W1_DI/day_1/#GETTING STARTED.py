#GETTING STARTED

#STRINGS METHODS
print("Hello world in python")

print("PYTHON is fun".lower())
#FIRST VALUE TYPE STRINGS METHODS
print('hello world in HTML'.replace('HTML','Python'))#this method gets arguments

#2ND VALUE TYPE:NUMBERS
#A) integers
a=5
b=6

print(type(a))

#8) floats:
5.5
3.484

print(5+8)
print(10-3.14)

my_age= 21
future_years= 123879
str_age=int(my_age)
print(type(my_age)) # '123879'

my_age_f=str_age+future_years
print(my_age_f)

print("Pythonic class \n"*4)

in_class=True
print(type(in_class))

my_name='David'
other_name='Shira'
print ('1st',my_name is my_name)
print ('2nd', 5<=3)
print ('3rd',5==3)
print ('4th',5=='5' is 5 or 3==3)
print ('5th',5 is 5 and 3==3)

bool_var=7383
print(bool(bool_var))

my_age=33

my_age -=12
print(my_age)

my_name='David'

my_name+='Attal'
print(my_name)
score=0
#code your game

score+=1

#FORMAT METHOD WAY
presentation='Hello,my name is {} and I am {} years old'.format(my_name,my_age)
print(presentation)
#F STRING WAY
#presentation=f'Hello,{my_name} is my_name and I am {my_age} years old'



#user_name=input('give me your name: ')
#user_age=int(input('give me your age:'))
#in_years=user_age+5
#print(in_years)


age = int(input("How old are you? "))
print(f"You are {age} years old")

if age is 18 or age>18:
    print('You are an adult')
elif 18>age>12:
    print('You are not an adult')
else:
    print("You are a child")

