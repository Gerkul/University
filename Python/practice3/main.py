
import re
def read_file(file_name):
    words = []

    with open(file_name, 'r', encoding="UTF-8") as file:
        for line in file.readlines():
            line = re.findall('[a-zа-яё]+', line, flags=re.IGNORECASE)
            for word in line:
                if word in words:
                    continue
                else:
                    words.append(word)

    return words


def save_file(file_name, words):
    with open(file_name, 'w', encoding="UTF-8") as file:
        for word in words:
            file.write(word + '\n')
        file.write(str(len(words)) + '\n')


words = read_file("text.txt")
words.sort()
print(words)

save_file("words.txt", words)
