from random import randrange

def increase_percents(was, became):
    return became * 100 / was - 100

number_of_doors = 3
probability_of_winning = 1 / number_of_doors

available_doors = [i + 1 for i in range(number_of_doors)]
print(available_doors)

player_number = int(input("Выбирите одну дверь двери из трёх(1, 2 или 3): "))

available_doors.remove(player_number)

show_host_number = randrange(1, 3)
while show_host_number == player_number:
    show_host_number = randrange(1, 3)

available_doors.remove(show_host_number)

print("Ведущий игры выбрал дверь под номером: ", show_host_number)

change_the_choise = input(f"Хотите ли вы выбрать дверь под номером {available_doors.pop()} (да/нет): ")

if change_the_choise == "да":
    print("Так как вы выбрали другую дверь, то вероятность того, что приз находится за этой "
          "дверью выше: ", increase_percents(probability_of_winning, 0.5))

if change_the_choise == "нет":
    print("Вероятность того, что приз за дверью, которую вы выбрали в первый раз "
          "меньше, чем если бы вы изменили свой выбор", probability_of_winning)