number = int(input())

vocab = {}

for i in range(number):
    lst = input().split(' ')
    if lst[0] in vocab:
        vocab[lst[0]] += int(lst[1])
    else:
        vocab[lst[0]] = int(lst[1])

lst_of_candidats = []
for key, value in vocab.items():
    lst_of_candidats.append(key)
lst_of_candidats = sorted(lst_of_candidats)

for key in lst_of_candidats:
    print(key, vocab[key])
