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

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r},author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise TypeError(f'Количество страниц не типа int: {new_pages!r}')
        if new_pages < 0:
            raise ValueError(f'Количество страниц меньше или равно 0: {new_pages!r}')
        self._pages = new_pages


class AudioBook(Book):
    """ Дочерний класс аудиокниги """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError(f'Продолжительность аудиокниги не типа float: {duration!r}')
        if duration < 0:
            raise ValueError(f'Продолжительность книги меньше или равна 0: {duration!r}')
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, float):
            raise TypeError(f'Продолжительность аудиокниги не типа float: {new_duration!r}')
        if new_duration < 0:
            raise ValueError(f'Продолжительность книги меньше или равна 0: {new_duration!r}')
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    Pbook = PaperBook("Книга_1", "Автор_1", 148)
    print(Pbook.pages)
    Pbook.pages = 841
    print(Pbook.pages)
    print(repr(Pbook))
    Abook = AudioBook("Книга_2", "Автор_2", 123.4)
    print(Abook.duration)
    Abook.duration = 432.1
    print(Abook.duration)
    print(repr(Abook))

