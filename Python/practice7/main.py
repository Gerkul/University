import csv


def get_books(with_name: str):
    books = []
    with open('books.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            if with_name.lower() in row[1].lower():
                books.append(row)

    return books


def get_totals(books):
    books_info = []

    for book_values in books:
        try:
            quantity_price = float(book_values[3]) * float(book_values[4])
            if quantity_price < 500:
                quantity_price += 100

            books_info.append((book_values[0], str(quantity_price)))
        except ValueError:
            print(f'Incorrect values in book ({book_values})')

    return books_info


books = get_books('python')
print(books)

books_info = get_totals(books)
print(books_info)
