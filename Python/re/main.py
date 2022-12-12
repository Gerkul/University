import re
from urllib import request

url_address = "https://msk.spravker.ru/avtoservisy-avtotehcentry"

html_file = request.urlopen(url_address)
html_string = html_file.read().decode()


name = r"(?:header__title-link\">)([^<]*)"

location = r"(?:[^.]*location\">\s*)([^\n]*)"

phone = r"(?:(?:[^.]*__value\">)(\+?\d.*\d\d[- ]?\d\d)(?:[^<]*))?"

opening = rf"(?:(?:[^.]*__value\">)((?:..[-,]..|ежедневно)(?:.*)(?:\d\d[ :]\d\d|круглосуточно))(?:[^<]*))?"

pattern = name + location + phone + opening

companies_list = re.findall(pattern, html_string)
print(companies_list)
print(len(companies_list))

companies_data = []

for item in companies_list:
    print(item)


