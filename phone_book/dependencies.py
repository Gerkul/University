def print_menu():
    print("1. Add contact")
    print("2. Delete contact by name")
    print("3. Viev phone book")
    print("4. Change phone number by name")
    print("5. Exit")
    print()

def normalize_phone_number(number):
    number = number.replace(' ', '').replace('-', '')
    if len(number) == 0:
        return '0'

    if number[:2] == '+7' and len(number) == 12:
        return number
    if number[0] == '8' and len(number) == 11:
        number = number.replace('8', '+7', 1)
        return number
    if number[0] == '9' and len(number) == 10:
        number = '+7' + number
        return number

    return '0'

def normalize_name(name):
    name.lower()
    name_surname = name.split(' ')

    if len(name_surname) < 2:
        return '0'

    name_surname[0] = name_surname[0].capitalize()
    name_surname[1] = name_surname[1].capitalize()

    name = name_surname[0] + ' ' + name_surname[1]

    return name

def input_name():
    name = normalize_name(input("Enter contact name: "))

    while name == '0':
        print("The name isn't correct. Please try again")
        name = normalize_name(input("Enter contact name: "))

    return name

def input_number():
    number = input("Enter contact phone number: ")
    number = normalize_phone_number(number)

    while number == '0':
        print("The number isn't correct. Please try again")
        number = input("Enter contact phone number: ")
        number = normalize_phone_number(number)

    return number

def input_data():
    name = input_name()
    phone_number = input_number()



    return [name, phone_number]



class PhoneBook:
    def __init__(self):
        self.book = {"Default Name": "89998889889"}


    def add_contact(self):
        data = input_data()

        if data[0] in self.book:
            act = input("The Name already exist. Do you want to replace phone number? 1/0: ")
            if int(act):
                self.book[data[0]] = data[1]
                print("The contact was changed")
        else:
            self.book[data[0]] = data[1]
            print("The contact was added")


    def delete_contact(self):
        name = input_name()

        if name in self.book:
            del self.book[name]
            print("The contact was deleted")
        else:
            print("The name '" + name + "' doesn't exist")


    def viev(self):
        print("\nViev phone book:")

        if len(self.book):
            for item in self.book.items():
                print(item[0], item[1])
        else:
            print("The phone book is empty")


    def change_phone_number(self):
        name = input_name()

        if name in self.book:
            number = input_number()
            self.book[name] = number
            print("The number was changed")
        else:
            print("Name", name, "is not exist. Please enter other name")