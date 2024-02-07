#XP Ninja
#3
'3 <= 3 < 9'#False
'3 == 3 == 3'#True
'bool(0)'#False
'bool(5 == "5")'#False
'bool(4 == 4) == bool("4" == "4")'#True
'bool(bool(None))'#False


x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

#print("x is", x)
#print("y is", y) 
#print("a:", a)
#print("b:", b)
#3

my_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit  esse cillum dolore eu fugiat nulla pariatur.  Excepteur sint occaecat cupidatat non proident,  sunt in culpa qui officia deserunt mollit anim id est laborum"
print(len(my_text))