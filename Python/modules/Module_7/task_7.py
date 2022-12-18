number = int(input())

words_vocab = {}

for i in range(number):
    lst = input().split(' ')
    for word in lst:
        if word in words_vocab:
            words_vocab[word] += 1
        else:
            words_vocab[word] = 1

sorted_words = sorted(words_vocab)
print(sorted_words)
for key in sorted_words:
    print(key, words_vocab[key])


