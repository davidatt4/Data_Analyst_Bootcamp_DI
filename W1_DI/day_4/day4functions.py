#functions
def say_hello(username,language):
    if language=="EN":
        print("Hello"+username)
    elif language=="FR":
        print("Bonjour"+username)
    else:
        print("This language is not supported"+language)

    
username="Rick"
language="FR"
say_hello(username="Rick", language="FR")
say_hello(language="FR", username="Rick")
say_hello("Rick", language="FR")


#Default values
def say_hello(username,language):
    if language=="EN":
        print("Hello"+username)
    elif language=="FR":
        print("Bonjour"+username)
    else:
        print("This language is not supported"+language)
    
#Local and global scope
#Local scope
def number_by_three(name, day):
  #local scope
  sentence = 'Hello {}! Today is {}.'.format(name, day)
  print(sentence)

#print(name)#impossible to use the variables from the local scope in the global scope


def square(number:int)->int:
    num_squared=number**2
    return num_squared

#print(square(2))


def country_info(country):
    if country =='Israel':
        population=963400
        capital='Jerusalem'
    if country=='Russia':
        population=143400000
        capital='Moskow'
    if country=='Brazil':
        population=214300000
        capital='Brasilia'

    return population,capital

print(country_info('Israel'))
a=country_info('Israel')
print(f'The population is {a}')

#exercice
def calculation(a:int,b:int)->tuple:
    add=a+b
    sub=a-b

    return add and sub
e,f=calculation(8,4)
print(e,f)