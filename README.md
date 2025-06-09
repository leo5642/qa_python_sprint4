-
### **TestBooksCollector1**  
**Тест**: `test_add_new_book_add_two_books`  
**Проверяет**:  
- Добавление двух книг в коллекцию  
- Корректность работы метода `get_books_rating()`  

### **TestBooksCollector2**  
**Тест**: `test_set_book_genre_add_two_books_and_genre`  
**Проверяет**:  
- Назначение жанров книгам через `set_book_genre()`  

### **TestBooksCollector3**  
**Тест**: `test_get_book_genre_add_book`  
**Проверяет**:  
- Возвращение жанра книги через `get_book_genre()`  

### **TestBooksCollector4**  
**Тест**: `test_get_books_with_specific_genre_add_three_books`  
**Проверяет**:  
- Фильтрацию книг по жанру через `get_books_with_specific_genre()`  

### **TestBooksCollector5**  
**Тест**: `test_get_books_genre`  
**Проверяет**:  
- Существование метода `get_books_genre`  

### **TestBooksCollector6**  
**Тест**: `test_get_books_for_children_add_two_book`  
**Проверяет**:  
- Возвращение книг с "безопасными" жанрами (без `'Ужасы'`)  

### **TestBooksCollector7-9**  
**Тесты**:  
7. `test_add_book_in_favorites_add_book`  
8. `test_delete_book_from_favorites_add_book_and_delete`  
9. `test_get_list_of_favorites_books`  
**Проверяют**:  
- Добавление/удаление книг в избранное.  
- Возвращение списка избранного.  
- Cделал проверку отсутствие возможности добавления в избранное при отсутвие книги в коллекции

