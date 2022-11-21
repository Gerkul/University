from random import randrange, randint

def the_monty_hall_paradox(number_of_iterations):

    probability_of_winning  = [0]

    for i in range(number_of_iterations):
        number_of_doors = randint(3, randint(100, 1000))
        probability = round(1 / number_of_doors, 5)

        available_doors = [i + 1 for i in range(number_of_doors)]

        player_number = randrange(1, number_of_doors)

        available_doors.remove(player_number)

        show_host_number = randrange(1, number_of_doors)
        while show_host_number == player_number:
            show_host_number = randrange(1, number_of_doors)

        available_doors.remove(show_host_number)

        change_the_choise = randrange(0, 2)

        if change_the_choise == 1:
            probability_of_winning.append(1 / len(available_doors) * 100 / probability - 100)

    return sum(probability_of_winning) / len(probability_of_winning)


if __name__ == "__main__":
    print(the_monty_hall_paradox(1000))