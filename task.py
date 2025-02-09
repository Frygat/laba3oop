class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

        @property
        def name(self) -> str:
            """Название книги(только для чтения)"""
            return self._name

        @property
        def author(self) -> str:
            """Автор книги(только для чтения"""
            return self._author

    """Строковое представление книги"""
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
    """Официальное представление книги"""
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """Класс для бумажной книги"""
        super().__init__(name, author)  #для вызова конструктора родительского класса
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц книги."""
        return self._pages
    @pages.setter
    def pages(self, value: int) -> None:
        """Устанавливает количество страниц книги"""

        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value < 1:
            raise ValueError("Количество страниц не может быть меньше 1.")
        self._pages = value

    def __str__(self) -> str:
        """Возвращает строковое представление бумажной книги."""
        f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """Конструктор для аудиокниг"""
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """Устанавливает продолжительность аудиокниги """

        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше 0.")
        self._duration = value

    def __str__(self) -> str:
         """Возвращает строковое представление аудиокниги."""
         return  f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"

if __name__ == "__main__":

    paper_book = PaperBook(name="semiconductor devices", author="Chirkin", pages=500)
    print(paper_book)
    print(repr(paper_book))

    audio_book = AudioBook(name="The Martian", author="Andy Weir", duration=12.5)
    print(audio_book)
    print(repr(audio_book)) 