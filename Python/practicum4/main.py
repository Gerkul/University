


file_name = input("Введите название файла: ")

file = open(file_name, 'r')

number_of_numbers = file.read()
print(number_of_numbers)

set_of_numbers = set()

for line in file.readlines():
    set.add(int(line))
    print(set.pop())