

running = True
while running:
    file_name = input("Введите название файла: ")

    try:
        file = open(file_name, 'r')
        number_of_numbers = file.readline()[:-1]
        numbers_list = []

        for number in file.readlines():
            if number.endswith('\n'):
                numbers_list.append(int(number[:-1]))
            else:
                numbers_list.append(int(number))

        if len(numbers_list) == number_of_numbers:
            raise Exception("Не правильное кол-во чисел в файле")

        running = False

    except FileNotFoundError:
        print("Такого файла нет")
    except ValueError:
        print("Не все элементы числа")
    except Exception as exception:
        print(exception)