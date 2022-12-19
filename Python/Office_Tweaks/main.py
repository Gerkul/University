from functions import *


current_path = os.getcwd()


while True:
    print_menu()
    action = input("Ваш выбор: ")

    if action == "0":
        current_path = change_dir()

    elif action == "1":
        convert_pdf_to_docx(current_path)

    elif action == "2":
        convert_docx_to_pdf(current_path)

    elif action == "3":
        convert_resize_img(current_path)

    elif action == "4":
        delete_files(current_path)

    elif action == "5":
        break

    print('\n' + current_path)


# change_dir()
# print(current_path)

