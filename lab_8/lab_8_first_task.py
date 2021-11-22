from lab_7_arkhipau import Book

# Задание 1
# Создайте класс «Библиотека». Используйте в нем список объектов типа
# «Книга» из предыдущего задания 1. Реализуйте в классе «Библиотека» следующие
# возможности:
# • добавление книги в библиотеку
# • удаление книги с заданными названием и автором из библиотеки
# • вывод всех книг, которые есть в библиотеке
# • поиск книги по автору
# • поиск книги по названию


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def removeBook(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                self.books.remove(book)
                break

    def printLibrary(self):
        for book in self.books:
            print(f"Book {book.name} by {book.author}")

    def findAuthorOfBook(self,author):
        for book in self.books:
            if book.author == author:
                print(f"Book {book.name} by {book.author}")

    def findNameOfBook(self,name):
        for book in self.books:
            if book.name == name:
                print(f"Book {book.name} by {book.author}")


my_lib = Library()
first = Book("Atlas Shrugged", "Ayn Rand", "Bloomsbury", "novel", 1957)
second = Book("Harry Potter", "J.K Rowling", "Bloomsbury", "fantasy", 1997)
third = Book("Harry Potter 2", "J.K Rowling", "Bloomsbury", "fantasy", 1997)
fourth = Book("Harry Potter", "J.B Rowling", "Bloomsbury", "fantasy", 1997)
my_lib.addBook(first)
my_lib.addBook(second)
my_lib.addBook(third) # для проверки, если есть несколько книг с одним автором
my_lib.addBook(fourth) # для проверки, если несколько книг имеют одно название

# my_lib.printLibrary()
#
# my_lib.removeBook("Harry Potter", "J.K Rowling") # убираю книгу
# print()
# my_lib.printLibrary()
# print()
# my_lib.findAuthorOfBook("J.K Rowling")
# print()
# my_lib.findNameOfBook("Harry Potter")



