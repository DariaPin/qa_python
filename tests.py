import pytest

from main import BooksCollector
class TestBooksCollector:

    def test_set_book_genre_existing_book(self):
        collector = BooksCollector() # Проверка добавления жанра к существующей книге
        collector.set_book_genre('Book1', 'Фантастика')
        assert collector.books_genre['Book1'] == 'Фантастика'

    def test_set_book_genre_add_genre_to_not_existing_book(self):
        collector = BooksCollector() # Проверка отказа от добавления жанра к несуществующей книге
        collector.set_book_genre('NonExistingBook', 'Детективы')
        assert 'NonExistingBook' not in collector.books_genre


    def test_set_book_genre_add_genre_to_not_acceptable_genre(self):
        collector = BooksCollector() # Проверка недопустимого жанра
        collector.set_book_genre('AnotherBook', 'Кулинария')
        assert 'AnotherBook' not in collector.books_genre


    def test_add_new_book_add_existing_book(self):
        collector = BooksCollector()
        name = "Повторное добавление"
        collector.add_new_book(name) # Первое добавление
        collector.add_new_book(name) # Повторное добавление
        # Проверяем, что значение словаря не изменилось после повторного добавления
        assert collector.books_genre[name] == ''

    def test_get_book_genre_valid_name(self):
        collector = BooksCollector()
        name = "Название книги"
        genre = "Жанр книги"
        collector.books_genre[name] = genre
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        name1 = "Название книги 1"
        genre = "Фантастика"
        collector.books_genre[name1] = genre

        name2 = "Название книги 2"
        collector.books_genre[name2] = genre

        # Проверяем, что функция корректно возвращает список названий книг для заданного жанра
        result = collector.get_books_with_specific_genre(genre)
        assert result == ["Название книги 1", "Название книги 2"]

    @pytest.mark.parametrize("name, genre", [
        ("Книга1", "Фантастика"),
        ("Книга2", "Детективы"),
        ("Книга3", "Комедии")
    ])
    def test_get_books_genre_dictionary(self, name, genre):
        collector = BooksCollector()

        # Добавляем книгу в словарь books_genre
        collector.books_genre[name] = genre
        result = collector.get_books_genre()
        assert result == {name: genre}

    def test_get_books_for_children_List_with_children_books(self):
        collector = BooksCollector()
        name1 = "Название книги 1"
        genre1 = "Комедии"

        # Добавляем книгу в словарь books_genre с жанром, подходящим для детей
        collector.books_genre[name1] = genre1

        name2 = "Название книги 2"
        genre2 = "Мультфильмы"

        # Проверяем, что функция корректно возвращает список названий книг для заданного жанра
        result = collector.get_books_for_children()
        assert result == [name1, name2]

    def test_add_book_to_favorites_book_in_favorites(self):
        collector = BooksCollector()
        name = "Название книги"

        # Добавляем книгу в словарь books_genre
        collector.books_genre[name] = "Комедии"

        # Проверяем, что книга добавлена в избранное
        assert name in collector.favorites

    def test_delete_book_from_favorites_book_not_in_favorites(self):
        collector = BooksCollector()

        # Создаём пустой список избранного
        collector.favorites = []

        # Добавляем две книги в словарь books_genre с разными жанрами
        name1 = "Первая книга"
        collector.books_genre[name1] = "Ужасы"
        name2 = "Вторая книга"
        collector.books_genre[name2] = "Мультфильмы"

        # Удаляем одну из книг из избранного
        collector.delete_book_from_favorites(name1)

        # Получаем актуальный список избранного
        result = collector.favorites

        # Убеждаемся, что одна из книг удалена из списка
        assert len(result) == 1
        assert name2 in result

    def test_get_list_of_favorites_books_get_list(self):
        collector = BooksCollector()
        collector.favorites = ["Book1", "Book2"]
        result = collector.get_list_of_favorites_books()
        assert result == ["Book1", "Book2"]