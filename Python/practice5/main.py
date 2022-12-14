import re

with open("text.txt", 'r', encoding="utf-8") as file:
    text = ''
    for line in file.readlines():
        text += line

    print(text)
    pattern = r"(Рейс \d{1,} (?:прибыл|отправился) (?:из|в) \w+ в \d\d:\d\d:\d\d)"
    train_list = re.findall(pattern, text)
    print(train_list)