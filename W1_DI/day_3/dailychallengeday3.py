#challenge 1
def create_letter_index_dict(word):
    letter_index_dict = {}

    for index, letter in enumerate(word):
        letter_str = str(letter)  # Ensure the letter is a string
        if letter_str in letter_index_dict:
            letter_index_dict[letter_str].append(index)
        else:
            letter_index_dict[letter_str] = [index]

    return letter_index_dict


user_word = input("Enter a word: ")
result_dict = create_letter_index_dict(user_word)
for key, value in result_dict.items():
    print(f"{key}: {value}")
#Challenge 2
def items_you_can_afford(wallet, store_items):
    affordable_items = []

    for item, price in store_items.items():
        if price <= wallet:
            affordable_items.append(item)

    affordable_items.sort()

    return affordable_items

# Example usage:
wallet_amount = float(input("Enter the amount of money in your wallet: "))

store_items = {
    'watch': 150,
    'shoes': 120,
    'pantalon': 40,
    'TV': 350,
    'phone': 999
}

affordable_items = items_you_can_afford(wallet_amount, store_items)

# Print the result
if affordable_items:
    print("You can afford the following items:")
    for item in affordable_items:
        print(item)
else:
    print("Nothing")
