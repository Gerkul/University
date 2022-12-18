number = int(input())

countries = {}

for i in range(number):
    lst = input().split(' ')
    countries[lst[0]] = lst[1:]

number = int(input())

cities = []

for i in range(number):
    cities.append(input())

for city in cities:
    for key, value in countries.items():
        for city_name in value:
            if city_name == city:
                print(key)
                break

