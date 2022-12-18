number = int(input())

vocab = {}

max_count = 0

for i in range(number):
    lst = input().split(' ')
    for word in lst:
        if word in vocab:
            vocab[word] += 1
        else:
            vocab[word] = 1

for key, value in vocab.items():
    if value > max_count:
        max_count = value

words_list = []

for key, value in vocab.items():
    if value == max_count:
        words_list.append(key)

words_list = sorted(words_list)

for key, value in vocab.items():
    if key == words_list[0]:
        print(key)
        break



