import pymorphy2
morph = pymorphy2.MorphAnalyzer()

words = []

import re

with open("text.txt", 'r', encoding="UTF-8") as file:
    for line in file.readlines():

        line = re.findall('[a-zа-яё]+', line, flags=re.IGNORECASE)
        for word in line:

            for item in morph.parse(word):
                words.append(item.normal_form)
                break

vocab = {}
for word in words:
    if word in vocab:
        vocab[word] += 1
    else:
        vocab[word] = 1

sorted_values = sorted(vocab.values(), reverse=True)
sorted_dict = {}

for i in sorted_values:
    for k in vocab.keys():
        if vocab[k] == i:
            sorted_dict[k] = vocab[k]

print(sorted_dict)

from translate import Translator
translator = Translator(to_lang="en", from_lang="ru")

eng_words = []
i = 0
for word in sorted_dict.keys():
    translation = translator.translate(word)
    eng_words.append(translation)
    print(word, translation)

    i += 1
    if i == 5:
        break

import csv
with open('words.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    i = 0
    print(len(eng_words))
    for key, value in sorted_dict.items():
        print(i)
        writer.writerow([key, eng_words[i], value])
        i += 1
        if i == 5:
            break



