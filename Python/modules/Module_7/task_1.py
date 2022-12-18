words_list = input().split(' ')

word_been = []

for word in words_list:
    print(word_been.count(word))
    word_been.append(word)
