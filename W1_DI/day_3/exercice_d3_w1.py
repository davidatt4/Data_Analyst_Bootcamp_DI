#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for a in zip(keys,values):
    print(a)

#2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for member, age in family.items():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    total_cost += ticket_price
    print(f"{member} has to pay ${ticket_price} for the ticket.")

print(f"\nThe total cost for the family is ${total_cost}.")


#3
# 2. Create a dictionary called brand with the given information
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': {'primary': 'pink', 'secondary': 'green'}
    }
}


brand['number_stores'] = 2


print(f"Zara's clients include men, women, children, and home shoppers.")


brand['country_creation'] = 'Spain'


if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')


del brand['creation_date']

print(f"The last international competitor is: {brand['international_competitors'][-1]}")
print(f"The major clothes colors in the US are: {brand['major_color']['US']}")
print(f"The number of key-value pairs in the dictionary is: {len(brand)}")
print(f"The keys of the dictionary are: {list(brand.keys())}")


more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}


print("\nOriginal Brand Dictionary:")
print(brand)
print("\nMore on Zara Dictionary:")
print(more_on_zara)

#4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
number_list=[0,1,2,3,4]
for item in zip(users,number_list):
    print(item)
#4b
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
number_list=[0,1,2,3,4]
for item in zip(number_list,users):
    print(item)
#4c
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_C = {}

for index, name in enumerate(sorted(users)):
    disney_users_C[name] = index

print(disney_users_C)

