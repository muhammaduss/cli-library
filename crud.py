class Book:
    """Класс Book необходим для crud операций с библиотекой.

    Заметка: причина по которой необходим всем атрибутам возможное пустое
    значение заключается в функции main.py получения всех книг, там мы создаем
    экземпляр без ничего, но мы все равно должны получить доступ к методам

    Атрибуты
    ---------
    id : int, optional
        уникальный айди книги
    title : str, optional
        название книги
    author : str, optional
        автор книги
    year : int, optional
        год издания
    status : str, optional
        статус книги (пусто либо "в наличии" либо "выдана")

    Методы
    -------
    add_to_library(library)
        добавление книги в библиотеку
    remove_from_library(library)
        удаление книги из библиотеки по id, берется с self
    retrieve_by_attr(library, search_attr, query)
        получение всех книг удовлетворяющих искомому аттрибуту и запросу
    retrieve_all
        получение списка всех книг
    update_status
        обновление статуса конкретной книги

    """

    def __init__(
        self,
        id: int = None,
        title: str = None,
        author: str = None,
        year: int = None,
        status: str = None,
    ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def add_to_library(self, library) -> None:
        library.append(
            {
                "id": self.id,
                "title": self.title,
                "author": self.author,
                "year": self.year,
                "status": self.status,
            }
        )

    def remove_from_library(self, library) -> bool:
        for i in library:
            if i["id"] == self.id:
                library.remove(i)
                return True
        return False

    def retrieve_by_attr(self, library, search_attr, query) -> bool:
        flag_if_found = False
        for i in library:
            if i[f"{search_attr}"] == query:
                flag_if_found = True
                print(i)
        return flag_if_found

    def retrieve_all(self, library) -> None:
        print("Список всех книг в библиотеке:")
        for i in library:
            print(i)
        print()

    def update_status(self, library) -> bool:
        for i in library:
            if i["id"] == self.id:
                i["status"] = self.status
                return True
        return False
