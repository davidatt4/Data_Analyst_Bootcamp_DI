#1
my_fav_numbers=[4,8,21,39,30]
my_fav_numbers.append(89)
my_fav_numbers.append(54)
my_fav_numbers.pop()
print(my_fav_numbers)
friends_fav_numbers=[13,2,4,0,67]
our_fav_numbers=my_fav_numbers+friends_fav_numbers
print(our_fav_numbers)

#2



#3
basket=["Banana","Apples","Oranges","Blueberries"]
basket.pop(0)
print(basket)
basket.pop(2)
print(basket)
basket.append("Kiwi")
print(basket)
basket[2]="Oranges"
basket[1]="Apples"
print(basket.count("Apples"))
basket.clear()
print(basket)
#4



#5
num_list=range(1,21)
for number in num_list:
    print(number)

for num in range(1,21):
    if num%2!=0:
        continue
    print(num)

#6
my_name="David"

while True:
    user_name=input("Please enter your name:")
    print(user_name)

    if user_name is my_name:
       print("Hello David!Nice to see you")
       break
    # else:
    #     print("Please enter a name:")

#7
# Ask the user to input their favorite fruit(s)
user_input_favorites = input("Enter your favorite fruit(s) separated by a single space: ")

# Split the input string into a list of favorite fruits
favorite_fruits = user_input_favorites.split()

# Display the list of favorite fruits
print("Your favorite fruits are:", favorite_fruits)

# Ask the user to input a name of any fruit
user_input_choice = input("Enter a fruit of your choice: ")

# Check if the user's input is in the list of favorite fruits
if user_input_choice in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")
#8
# Initialize an empty list to store pizza toppings
toppings = []

# Constant price for the pizza base
base_price = 10

# Constant price per topping
topping_price = 2.5

# Loop to ask the user for pizza toppings
while True:
    # Ask the user to enter a topping or 'quit' to stop
    user_input = input("Enter a pizza topping (or 'quit' to finish): ")

    # Check if the user wants to quit
    if user_input.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    # Add the topping to the list
    toppings.append(user_input)
    
    # Print a message confirming the addition of the topping
    print(f"Adding {user_input} to your pizza.")

# Calculate the total price of the pizza
total_price = base_price + len(toppings) * topping_price

# Print the list of toppings and the total price
print("\nYour pizza toppings:")
for topping in toppings:
    print("- " + topping)
print("\nTotal Price: $", total_price)
#9
# Function to calculate ticket price based on age
def calculate_ticket_price(age):
    if age < 3:
        return 0  # Ticket is free for children under 3
    elif 3 <= age <= 12:
        return 10  # Ticket is $10 for ages 3 to 12
    else:
        return 15  # Ticket is $15 for ages over 12

# Ask a family for the age of each person who wants a ticket
num_people = int(input("Enter the number of people in the family: "))
total_cost = 0

for _ in range(num_people):
    age = int(input("Enter the age of a person: "))
    ticket_price = calculate_ticket_price(age)
    total_cost += ticket_price

# Print the total cost of all the family's tickets
print("Total cost of family's tickets: $", total_cost)

# Group of teenagers wanting to watch a restricted movie
teenagers = ["Alice", "Bob", "Charlie", "David", "Emma"]

# Remove teenagers who are not permitted to watch the movie
allowed_age_range = range(16, 22)
teenagers = [name for name in teenagers if int(input(f"Enter {name}'s age: ")) in allowed_age_range]

# Print the final list of teenagers permitted to watch the movie
print("Final list of teenagers permitted to watch the movie:", teenagers)
#10
# Initial list of sandwich orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# Remove all occurrences of "Pastrami sandwich" using a while loop
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Prepare the orders of the clients
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Remove the first sandwich from the list
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich.lower()}")

# Print a message listing each sandwich that was made
print("\nList of sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.lower()}")
