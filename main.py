import json
import os.path
from crud import Book

"""
    Ниже - функции обертки перед вызовом методов класса,
    про эти методы внутри самого класса. Это было сделано
    для реккурентного вызова функций (на случай невалидного инпута)
"""


def add_book_to_library(library) -> None:
    while 1:
        title = str(input("Введите название книги: "))
        author = str(input("Введите автора книги: "))
        year = str(input("Введите год издания: "))
        id: int = 1 if not library else library[-1]["id"] + 1
        if not year.isdigit():
            print("Введите корректный год")
        else:
            year = int(year)
            break

    book = Book(id, title, author, year, "в наличии")
    book.add_to_library(library)

    with open("library.json", "w", encoding="utf-8") as f:
        json.dump(library, f, ensure_ascii=False, indent=4)

    print("\nКнига успешно добавлена.\n")


def remove_book_from_library(library) -> None:
    id = int(input("Введите id книги, которую необходимо удалить: "))
    book = Book(id)

    if book.remove_from_library(library):
        with open("library.json", "w", encoding="utf-8") as f:
            json.dump(library, f, ensure_ascii=False, indent=4)

        print("\nКнига успешно удалена.\n")
    else:
        opt = int(
            input(
                "\nПростите, книги с данным id, вероятно, не существует"
                "\n[1] Вернуться\n[2] Ввести id заново\n"
            )
        )
        if opt == 1:
            return
        else:
            remove_book_from_library(library)


def retrieve_book_by_attr(library) -> None:
    while 1:
        search_attr = str(
            input(
                "Выберите, по какому атрибуту вы"
                "хотите найти книгу (title|author|year): "
            )
        )
        if search_attr != "title" and search_attr != "author" and search_attr != "year":
            print("Пожалуйста, введите корректный атрибут")
        else:
            break

    query = str(input())
    if query.isdigit():
        query = int(query)

    book = Book()

    if book.retrieve_by_attr(library, search_attr, query):
        print()
    else:
        opt = int(
            input(
                "Такой книги нет в библиотеке, попробуйте найти "
                "другую\n[1] Вернуться\n[2] Найти другую книгу\n"
            )
        )
        if opt == 1:
            return
        else:
            retrieve_book_by_attr(library)


def retrieve_all_books(library):
    book = Book()
    book.retrieve_all(library)


def update_book_status(library) -> None:
    id = int(input("Введите пожалуйста id: "))
    while 1:
        status = str(input("Введите новый статус (в наличии | выдана): "))

        if status != "в наличии" and status != "выдана":
            print("Такой статус невозможен")
        else:
            break

    book = Book(id=id, status=status)

    if book.update_status(library):
        with open("library.json", "w", encoding="utf-8") as f:
            json.dump(library, f, ensure_ascii=False, indent=4)
        print("Статус успешно обновлен\n")
    else:
        opt = int(
            input(
                "Книги с таким id не существует\nВыберите:\n"
                "[1] Вернуться\n[2] Ввести другой id"
            )
        )
        if opt == 1:
            return
        else:
            update_book_status(library)


def option_handler(option, library):
    """
    Функция для изымания логики определения выбора юзера в меню с main
    """
    if option == 1:
        add_book_to_library(library)
    elif option == 2:
        remove_book_from_library(library)
    elif option == 3:
        retrieve_book_by_attr(library)
    elif option == 4:
        retrieve_all_books(library)
    elif option == 5:
        update_book_status(library)


if __name__ == "__main__":
    try:
        if os.path.isfile("./library.json"):
            with open("library.json", "r", encoding="utf-8") as f:
                library = json.load(f)
        else:
            library = []
    except Exception as e:
        print(e)

    # Бесконечная обработка юзера, останавливается при соответствующем инпуте
    while 1:
        print(
            "Выберите действие (число):\n[1] Добавить книгу\n"
            "[2] Удалить книгу\n[3] Найти книги\n[4] Отобразить все книги\n"
            "[5] Изменить статус книги"
        )
        option = int(input())
        option_handler(option, library)

        opt = int(
            input(
                "Выберите действие (число):\n"
                "[1] Вернуться в меню\n[2] Завершить программу\n"
            )
        )
        if opt == 2:
            break
