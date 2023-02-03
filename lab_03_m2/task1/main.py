class Book:
    """ Базовый класс книги """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    """ Дочерний класс бумажной книги """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError(f'Количество страниц не типа int: {pages!r}')
        if pages < 0:
            raise ValueError(f'Количество страниц меньше или равно 0: {pages!r}')
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}\nКоличество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс аудиокниги """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError(f'Продолжительность аудиокниги не типа float: {duration!r}')
        if duration < 0:
            raise ValueError(f'Продолжительность книги меньше или равна 0: {duration!r}')
        self.duration = duration

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}\nПродолжительность книги: {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
