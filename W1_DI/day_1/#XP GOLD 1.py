#XP GOLD 1
print("Hello World\n"*4+"I love python\n"*4)

#2
number_month= int(input("Please enter a number beetween 1 and 12:"))
print(type(number_month))
if 3 <=number_month<=5:
    print("Spring")
elif 6 <=number_month<=8:
    print("Summer")
elif 9 <=number_month<=11:
    print("Autumn")
elif number_month==12 or 1<=number_month<=2:
    print("Winter")