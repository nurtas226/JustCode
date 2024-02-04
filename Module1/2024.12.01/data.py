from books import Book
from libraries import Library
from users import User


def get_library_with_books():
    library = Library()

    book1 = Book('Roman Stroies', 'Jhumpa Lahiri', 'Fiction')
    book2 = Book('1984', 'George Orwell', 'Fiction')
    book3 = Book('Deep Thinking', 'Garry Kasparov', 'Non-Fiction')
    book4 = Book('Fear is just a word', 'Azam Ahmed', 'Fiction')
    book5 = Book('Judment at Tokyo', 'Gary J. Bass', 'Non-Fiction')
    book6 = Book('Wrong Way', 'Joanne Mcneil', 'Fiction')

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)

    return library