lst = [int(s) for s in input().split()]

for i in range(len(lst) - 1):
    if lst[i + 1] > lst[i]:
        print(lst[i + 1])
