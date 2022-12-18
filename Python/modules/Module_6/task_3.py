lst = [int(s) for s in input().split()]
new_lst = []
for i in range(0, len(lst) - 1, 2):
    new_lst.append(lst[i + 1])
    new_lst.append(lst[i])
if len(lst) % 2 != 0:
    new_lst.append(lst[-1])

for item in new_lst:
    print(item)
