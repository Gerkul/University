import re

train_list = []

with open("text.txt", 'r', encoding="utf-8") as file:
    text = ''
    for line in file.readlines():
        text += line

    pattern = r"(Рейс \d{1,} (?:прибыл|отправился) (?:из|в) \w+ в \d\d:\d\d:\d\d)"
    train_list = re.findall(pattern, text)


pattern2 = r"([^.]*)(?: в )(\d\d:\d\d:\d\d)"

with open("saved_data.txt", "w", encoding="utf-8") as file:
    for note in train_list:
        data_to_save = re.findall(pattern2, note)

        data_of_train = re.findall(r"(Рейс )(\d\d\d )(?:\w+ )(из|в)( \w+)", data_to_save[0][0])
        data_of_train = "Поезд " + '№' + ' ' + data_of_train[0][1] + data_of_train[0][2] + data_of_train[0][3]

        file.write('['+data_to_save[0][1]+']' + " - " + data_of_train + '\n')

