from users import User
from books import Book
from libraries import Library
from data import get_library_with_books

library = get_library_with_books()

maxim = User('Max')
book_return = Library()

print(f"Welcome to our library!\n")
user_input = None

while user_input != 'q':
    print("\nMenu:\n"
          "1. All available books\n"
          "2. Take a book\n"
          "3. Your books\n"
          "4. Return a book\n"
          "5. Find books by genre")

    user_input = input("\nChoose [1-2] from menu ('q' = exit): ")

    if user_input == '1':
        books = library.get_available_books()
        for i in range(len(books)):
            print(f"{i}. {books[i]}")
    elif user_input == '2':
        books = library.get_available_books()
        for i in range(len(books)):
            print(f"{i}. {books[i]}")

        ind = int(input("Choose a book: "))

        maxim.take_book(books[ind])
        print("Enjoy reading!\n\n")
    elif user_input == '3':
        taken_books = maxim.get_taken_books()
        print("Your books: ")
        for i in range(len(taken_books)):
            print(f"{i}. {taken_books[i]}")
    elif user_input == '4':
        returns = maxim.get_taken_books()
        for i in range(len(returns)):
            print(f"{i}. {returns[i]}")
            
        ind = int(input("Choose a book from your books: "))
        
        book_return.add_book(returns[ind])
    elif user_input == '5':
        genres = library.get_genres()
        for i in range(len(genres)):
            print(f"{i}. {genres[i]}")
            
        ind = int(input("Choose a genre by index: "))
        
        if ind < len(genres):
            selected_genre = genres[ind]
            sorted_books = library.find_books_by_genre(selected_genre)
            if sorted_books:
                print(f"\nBooks in the selected genre {selected_genre}: ")
                for book in sorted_books:
                    print(book)
        
    elif user_input == 'q':
        print("Hope you come back!")
    else:
        print("Undefined option, please choose from menu!\n\n")