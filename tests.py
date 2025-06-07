from main import BooksCollector

# TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # слooks_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

class TestBooksCollector2:
    def test_set_book_genre_add_two_books_and_genre(self):#2
        
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')

        assert collector.books_genre['Гордость и предубеждение и зомби'] ==  'Ужасы'
        assert collector.books_genre['Что делать, если ваш кот хочет вас убить'] ==  'Комедии'


class TestBooksCollector3:
    def test_get_book_genre_add_book(self):#3
        
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
    
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Гордость и предубеждение и зомби'


class TestBooksCollector4:
    def test_get_books_with_specific_genre_add_three_books(self):#4
        
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Горе от ума', 'Комедии')

        assert len(collector.get_books_with_specific_genre('Ужасы')) == 1
        assert len(collector.get_books_with_specific_genre('Комедии')) == 2
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 0


class TestBooksCollector5:
    def test_get_books_genre(self):#5
        
        collector = BooksCollector()

        collector.get_books_genre

        assert books_genre != ''


class TestBooksCollector6:
    def test_get_books_for_children_add_two_book(self):#6
        
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')

        assert collector.get_books_for_children in 'Что делать, если ваш кот хочет вас убить'
        assert not collector.get_books_for_children in 'Гордость и предубеждение и зомби'


class TestBooksCollector7:
    def test_add_book_in_favorites_add_book(self):#7
        
        collector = BooksCollector()
        
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert collector.favorites == 'Гордость и предубеждение и зомби'


class TestBooksCollector8:
    def test_delete_book_from_favorites_add_book_and_delete(self):#8

        collector = BooksCollector()
        
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert collector.favorites == ''


class TestBooksCollector9:
    def test_get_list_of_favorites_books(self):#9

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert collector.favorites == 'Гордость и предубеждение и зомби'
