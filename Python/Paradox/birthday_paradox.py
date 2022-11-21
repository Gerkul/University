import random

def birthday_paradox(number_of_iterations):
    number_of_people = random.randint(1, 100)
    days   = [day + 1   for day in   range(28)]
    months = [month + 1 for month in range(12)]

    number_of_coincidences = 0
    number_of_mismatches   = 0

    for iterations in range(number_of_iterations):
        birthday_days   = [random.choice(days)   for _ in range(number_of_people)]
        birthday_months = [random.choice(months) for _ in range(number_of_people)]

        for i in range(number_of_people):
            count_mismatches = 0

            for j in range(number_of_people):
                if j != i and birthday_days[j]   == birthday_days[i] and \
                   birthday_months[j] == birthday_months[i]:
                    number_of_coincidences += 1
                    count_mismatches += 1

            if count_mismatches == 0:
                number_of_mismatches += 1

    probability_of_coincidences = number_of_coincidences / number_of_people * number_of_iterations
    return probability_of_coincidences

if __name__ == "__main__":
    birthday_paradox(1)