lst1 = [int(s) for s in input().split()]
lst2 = [int(s) for s in input().split()]

new_lst = []

for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i] == (lst2[j]):
            new_lst.append(lst1[i])

print(sorted(new_lst))
