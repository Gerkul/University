import re
from typing import List, Any


def read_file(file_name):
    words= []

    with open(file_name, 'r', encoding="UTF-8") as file:
        for line in file.readlines():
            line = re.findall('[a-zа-яё]+', line, flags=re.IGNORECASE)
            for word in line:
                if word.lower() in words:
                    continue
                else:
                    words.append(word.lower())

    return words


def save_file(file_name, words):
    with open(file_name, 'w', encoding="UTF-8") as file:
        file.write("Всего уникалных слов: " + str(len(words)) + '\n')
        file.write("======================" + '\n')
        for word in words:
            file.write(word + '\n')


words = read_file("data.txt")
words.sort()

save_file("words.txt", words)
