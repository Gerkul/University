lst = [int(s) for s in input().split()]
min_num = lst[0]
max_num = lst[0]
min_index = 0
max_index = 0


for i, n in enumerate(lst):
    if n < min_num:
        min_num = n
        min_index = i

    if n > max_num:
        max_num = n
        max_index = i

lst[min_index] = max_num
lst[max_index] = min_num

print(lst)