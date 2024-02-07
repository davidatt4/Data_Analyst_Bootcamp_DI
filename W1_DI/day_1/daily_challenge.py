#Daily challenge

str_number=input("Please enter a text:")
print(type(str_number))
if len(str_number)<10:
    print("string not long enough")
elif len(str_number)>10:
    print("string too long")
else:
    print("perfect string")

first_character=str_number[0]
last_character=str_number[-1]
print("First Character",first_character)
print("Last_Character",last_character)

my_string="David"
for i in range (1,len(my_string)+1):
    print(my_string[:i])
import random
my_string="Hello World"
shuffled_list=list(my_string)
random.shuffle(shuffled_list)
shuffled_string=''.join(shuffled_list)
print(shuffled_string)

#Correction
import random
user_str=input("Give me a string 10 chars long:")
if len(user_str)<10:
    print("string not long enough")
elif len(user_str)>10:
    print("string too long")
else:
    print("perfect string")
    print ('thats the first and last chars:',user_str[0],user_str[-1])

