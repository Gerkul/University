number = int(input())
vocab = {}

for i in range(number):
    lst = input().split(' ')
    vocab[lst[0]] = lst[1]

search_value = input()

for key, value in vocab.items():
    if value == search_value:
        print(key)