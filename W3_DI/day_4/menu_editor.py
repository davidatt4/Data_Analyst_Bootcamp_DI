from menu_item import MenuItem
from menu_manager import MenuManager
class MenuEditor:
    def show_user_menu():
        print("Program Menu:")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("X - Exit")

        choice = input("Enter your choice: ").upper()

        if choice == 'V':
            MenuEditor.view_item()
        elif choice == 'A':
            MenuEditor.add_item_to_menu()
        elif choice == 'D':
            MenuEditor.remove_item_from_menu()
        elif choice == 'U':
            MenuEditor.update_item_from_menu()
        elif choice == 'S':
            MenuEditor.show_restaurant_menu()
        elif choice == 'X':
            MenuEditor.show_restaurant_menu()
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please try again.")

    def add_item_to_menu():
        item_name = input("Enter the item's name: ")
        item_price = float(input("Enter the item's price: "))

        new_item = MenuItem(item_name, item_price)
        new_item.save()
        print("Item was added successfully.")
    def remove_item_from_menu():
        item_name = input("Enter the name of the item to remove: ")

        item_to_remove = MenuManager.get_by_name(item_name)

        if item_to_remove:
            item_to_remove.delete()
            print("Item was deleted successfully.")
        else:
            print("Error: Item not found.")

    def update_item_from_menu():
        item_name = input("Enter the name of the item to update: ")
        new_item_name = input("Enter the new name for the item: ")
        new_item_price = float(input("Enter the new price for the item: "))

        item_to_update = MenuManager.get_by_name(item_name)

        if item_to_update:
            item_to_update.update(new_name=new_item_name, new_price=new_item_price)
            print("Item was updated successfully.")
        else:
            print("Error: Item not found.")

    def view_item():
        item_name = input("Enter the name of the item to view: ")

        item_to_view = MenuManager.get_by_name(item_name)

        if item_to_view:
            print(item_to_view)
        else:
            print("Error: Item not found.")

    
    def show_restaurant_menu():
        print("\nRestaurant Menu:")
        items = MenuManager.all_items()
        for item in items:
            print(item)

if __name__ == "__main__":
    while True:
        MenuEditor.show_user_menu()