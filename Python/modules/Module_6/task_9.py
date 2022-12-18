string = input()

str1 = string[:int(len(string) / 2 + 1)]
str2 = string[int(len(string) / 2 + 1):]

print(str2 + str1)

