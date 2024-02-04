from books import Book
from libraries import Library
from users import User


library = Library()

book1 = Book('Roman Stroies', 'Jhumpa Lahiri', 'Fiction')
book2 = Book('1984', 'George Orwell', 'Fiction')
book3 = Book('Deep Thinking', 'Garry Kasparov', 'Non-Fiction')
book4 = Book('Fear is just a word', 'Azam Ahmed', 'Fiction')
book5 = Book('Judment at Tokyo', 'Gary J. Bass', 'Non-Fiction')
book6 = Book('Wrong Way', 'Joanne Mcneil', 'Fiction')

library.add_book(book1)
library.add_book(book2)

maxim = User('Max')

print("In library: ", library.get_available_books())
print("Max owns: ", maxim.get_books())

print("\nMax taking a book from library\n")
maxim.take_book(book1)

print("In library: ", library.get_available_books())
print("Max owns: ", maxim.get_books())

print("\nMax returing a book...\n")
maxim.return_book(book1)

print("In library: ", library.get_available_books())
print("Max owns: ", maxim.get_books())

print(len(library))