string = input()

str1 = string[:string.find('h')]
str2 = string[string.rfind('h')+1:]

print(str1 + str2)