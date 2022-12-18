string = input()

for i in range(string.find('h') + 1, string.rfind('h')):
    if string[i] == 'h':
        string = string[:i] + 'H' + string[i + 1:]

print(string)