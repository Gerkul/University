lst = [int(s) for s in input().split()]

num_been = []

for n in lst:
    if n in num_been:
        print("ДА")
    else:
        print("НЕТ")

    num_been.append(n)
