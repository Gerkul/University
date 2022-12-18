number = int(input())

files = {}

operations = {
    'read': "R",
    'write': "W",
    'execute': "X"
}

for i in range(number):
    lst = input().split(' ')
    files[lst[0]] = lst[1:]

number = int(input())

for i in range(number):
    lst = input().split(' ')
    if operations[lst[0]] in files[lst[1]]:
        print("OK")
    else:
        print("Denied")

