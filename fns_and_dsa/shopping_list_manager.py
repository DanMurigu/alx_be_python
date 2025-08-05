def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # prompt for user to add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to your shopping list. \n")

        elif  choice == '2':
            #prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.\n")
            else:
                print(f"{item}Is not on the list.\n")
        
        elif choice == '3':
            if shopping_list:
            #Display the shopping list
                print("Your shopping list:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
                print()
            else:
                print("Your shopping list is empty. \n")
                
        elif choice == '4':
            print ("Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()      


