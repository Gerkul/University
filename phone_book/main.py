from dependencies import print_menu, PhoneBook

def main():
    is_run = True

    phone_book = PhoneBook()

    while is_run:
        print_menu()

        act = input("Enter your action: ")

        try:
            act = int(act)
        except ValueError:
            pass

        if act == 1:
            phone_book.add_contact()
        elif act == 2:
            phone_book.delete_contact()
        elif act == 3:
            phone_book.viev()
        elif act == 4:
            phone_book.change_phone_number()
        elif act == 5:
            is_run = False
            print("Goodby")
        else:
            print("The menu item didn't recognize. Please enter correct action")
        print("\n")

main()

