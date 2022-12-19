import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image


def print_menu():
    print("0. Сменить рабочий каталог")
    print("1. Преобразовать PDF в Docx")
    print("2. Преобразовать Doc/Docx в PDF")
    print("3. Произвести сжатие изображений")
    print("4. Удалить группу файлов")
    print("5. Выход")


def change_dir():
    new_dir_name = input("Введине название директории: ")
    os.chdir(rf"{new_dir_name}")
    return os.getcwd()


def convert_pdf_to_docx(dir_path):
    pdf_paths = []
    for dir_item in os.listdir(dir_path):
        path = dir_path + '\\' + dir_item
        if os.path.isfile(path) and path.endswith(".pdf"):
            pdf_paths.append(dir_item)

    for i, name in enumerate(pdf_paths):
        print(i, name)
    print(len(pdf_paths), "преобразовать все файлы")

    index = int(input("Введите номер файла для преобразования: "))

    if index == len(pdf_paths):
        for i, name in enumerate(pdf_paths):
            pdf_file = pdf_paths[i]
            docx_file = pdf_paths[i][:-4] + ".docx"
            cv = Converter(pdf_file)
            cv.convert(docx_file)

    elif index > -1 and index < len(pdf_paths):
        pdf_file = pdf_paths[index]
        docx_file = pdf_paths[index][:-4] + ".docx"

        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()


def convert_docx_to_pdf(dir_path):
    docxs_path = []
    for dir_item in os.listdir(dir_path):
        path = dir_path + '\\' + dir_item
        if os.path.isfile(path) and path.endswith(".docx"):
            docxs_path.append(dir_item)

    for i, name in enumerate(docxs_path):
        print(i, name)
    print(len(docxs_path), "преобразовать все файлы")

    index = int(input("Введите номер файла для преобразования: "))

    if index == len(docxs_path):
        for i, name in enumerate(docxs_path):
            docx_file = docxs_path[i]
            pdf_file = docxs_path[i][:-5] + "1.pdf"
            convert(docxs_path + '\\')

    elif index > -1 and index < len(docxs_path):
        docx_file = docxs_path[index]
        print(docx_file)
        convert(docx_file)


def resize_img(img, delta):
    width_size = int(img.size[0] * delta / 100)
    height_size = int(img.size[0] * delta / 100)
    new_image = img.resize((width_size, height_size))
    return new_image


def convert_resize_img(dir_path):
    percent = input("Введите процент сжатия изображения от 1 до 100: ")
    try:
        percent = int(percent)
    except ValueError:
        percent = -1

    while not (percent > 0 and percent < 101):
        percent = input("Введите процент сжатия изображения от 1 до 100: ")
        try:
            percent = int(percent)
        except ValueError:
            percent = -1

    imgs_path = []
    for dir_item in os.listdir(dir_path):
        try:
            with Image.open(dir_item) as im:
                imgs_path.append(dir_item)
        except OSError:
            pass

    for i, name in enumerate(imgs_path):
        print(i, name)
    print(len(imgs_path), "преобразовать все файлы")

    index = int(input("Введите номер файла для преобразования: "))

    if index == len(imgs_path):
        for img_path in imgs_path:
            img = Image.open(img_path)
            resize_img(img, percent).save("resize_" + img_path)

    elif index > -1 and index < len(imgs_path):
        img = Image.open(imgs_path[index])
        resize_img(img, percent).save("resize_" + imgs_path[index])


def delete_files(dir_path):
    print("0. Удалить все файлы, начинающиеся на определенную подстроку")
    print("1. Удалить все файлы, заканчивающиеся на определенную подстроку")
    print("2. Удалить все файлы содержащие определенную подстроку")
    print("3. Удалить все файлы по расширению")

    action = input()

    files_paths = []

    for dir_item in os.listdir(dir_path):
        path = dir_path + '\\' + dir_item
        if os.path.isfile(path):
            files_paths.append(dir_item)

    files_to_delete = []

    if action == "0":
        string = input("Введите подстроку")
        for path in files_paths:
            if path.startswith(string):
                files_to_delete.append(path)

    elif action == "1":
        string = input("Введите подстроку")
        for path in files_paths:
            if path.endswith(string):
                files_to_delete.append(path)

    elif action == "2":
        string = input("Введите подстроку")
        for path in files_paths:
            if string in path:
                files_to_delete.append(path)

    elif action == "3":
        string = input("Введите формат")
        for path in files_paths:
            if path.endswith(string):
                files_to_delete.append(path)

    for file in files_to_delete:
        path = dir_path + '\\' + file
        os.remove(path)


# convert_pdf_to_docx(os.getcwd())
# convert_docx_to_pdf(os.getcwd())
# convert_resize_img(os.getcwd(), 50)
# delete_files(os.getcwd())


