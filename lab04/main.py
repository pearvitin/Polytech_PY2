if __name__ == "__main__":
    class Media:
        """
        Базовый класс Медиатека

        :param name – Название(зарегистрированное, а не имя файла)
        :param age_limit - Возрастное ограничение

        """
        def __init__(self, name: str, age_limit: int):
            self._name = name
            if not isinstance(age_limit, int):
                raise TypeError(f'Возрастное ограничение не типа int: {age_limit!r}')
            if age_limit < 0:
                raise ValueError(f'Возрастное ограничение меньше 0: {age_limit!r}')
            self._age_limit = age_limit

        def __str__(self):
            return f"Название: {self.name}\nВозрастное ограничение: {self.age_limit}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, author={self.age_limit!r})"

        def age_check(self, entered_age):  # Наследуется для всех дочерних кдассов
            """Функция проверки соответствия введенного возраста возрастному ограничению"""
            if entered_age < self._age_limit:
                print(f'Медиа-файл не предназначен к просмотру лицам, не достигшим возраста {self._age_limit!r} лет')
            else:
                print('Просмотр медиа-файла разрешен')

        def add_comment(self):  # Наследуется для всех дочерних кдассов
            """Функция позволяет добавить свой комментарий/пометку к файлу"""
            ...
            pass

        @property  # Название произведения неизменно, является уникальным идентификатором
        def name(self):
            return self._name

        @property  # Возрастное ограничение медиа-файла фиксирована
        def age_limit(self):
            return self._age_limit

    class Movie(Media):
        """

        Дочерний класс Фильм

        :param duration – Длительность фильма
        :param annotation – Аннотация к фильму файла. Может не задаваться

        """

        def __init__(self, name: str, age_limit: int, duration: float, annotation=None):
            super().__init__(name, age_limit)
            if isinstance(duration, int):
                duration = float(duration)
            if not isinstance(duration, float):
                raise TypeError(f'Длительность не типа int: {duration!r}')
            if age_limit < 0:
                raise ValueError(f'Длительность меньше 0: {duration!r}')
            self._duration = duration
            self.annotation = annotation

        def __str__(self):  # Посчитал нужным переназначить str из-за появления анотации
            return f"Название: {self.name}\nВозрастное ограничение: {self.age_limit}\nАннотация: {self.annotation}"

        def __repr__(self):  # Переназначен из-за дополнительных аргументов
            return f"{self.__class__.__name__}(name={self.name!r}," \
                   f"age_limit={self.age_limit!r}, annotation={self.annotation!r},duration={self.duration!r})"

        def make_clip(self, start, end):
            """Функция возвращает новое значение duration для отрезка фильма"""
            self._duration = end - start
            return self._duration

        @property  # Длительность медиа-файла фиксирована
        def duration(self):
            return self._duration


    class Audio(Media):

        """
        Дочерний класс аудио

        :param duration – Длительность фильма
        :param author – Аннотация к фильму файла. Может не задаваться

        """

        def __init__(self, name: str, age_limit: int, duration: float, author=None):
            super().__init__(name, age_limit)
            if isinstance(duration, int):
                duration = float(duration)
            if not isinstance(duration, float):
                raise TypeError(f'Длительность не типа int: {duration!r}')
            if age_limit < 0:
                raise ValueError(f'Длительность меньше 0: {duration!r}')
            self._duration = duration
            if author is None:
                author = 'Неизвестен'
            if not isinstance(author, str):
                raise TypeError(f'Автор не типа str: {author!r}')
            self._author = author

        def __repr__(self):  # Переназначен из-за новых аргументов
            return f"{self.__class__.__name__}(name={self.name!r}, age_limit={self.age_limit!r}," \
                   f" author={self.author!r}, author={self.author!r})"

        @property  # Автор аудиозаписи фиксирован
        def author(self):
            return self._author

        @property   # Длительность аудиозаписи фиксирована
        def duration(self):
            return self._duration

        @author.setter  # Если автор изначально не указан, поддерживается многоразовая смена записи об авторстве
        def author(self, new_author):
            if self.author is not None:
                raise TypeError('Невозможно изменить автора, если он установлен')
            if isinstance(new_author, str):
                raise TypeError('Автор должен быть типа str')
            self._author = new_author


    class Photo(Media):

        """
        Дочерний класс Фото

        Без новых параметров

        """

        def __init__(self, name: str, age_limit: int):
            super().__init__(name, age_limit)

    pass
