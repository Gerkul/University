import random


def birthday_paradox(people_count, iterations_count = 1000):
    days = [day for day in range(29)]
    months = [month for month in range(13)]

    count_coincidences = 0
    count_not_coincidences = 0

    for iterations in range(iterations_count + 1):
        d_data = []
        m_data = []

        for i in range(people_count + 1):
            d_data.append(random.choice(days))
            m_data.append(random.choice(months))

        for i in range(0, people_count):
            if d_data.count(d_data[i]) == 1 or m_data.count(m_data[i]) == 1:
                count_not_coincidences += 1
                pass

            for j in range(0, people_count):
                if j == i:
                    pass

                if d_data[j] == d_data[i] and m_data[j] == m_data[i]:
                    count_coincidences += 1

    return f"количество совпадений: {count_coincidences} " \
           f"количество не совпадений: {count_not_coincidences} " \
           f"вероятность совпадения: {(count_coincidences * 100) / (count_not_coincidences + count_coincidences)}"