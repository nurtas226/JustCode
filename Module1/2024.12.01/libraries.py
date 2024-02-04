
class Library():
    
    def __init__(self):
        self.book_storage = []

    def add_book(self, new_book):
        """
        adds object of Book to self.book_storage
        :param new_book: Book
        :return: None
        """
        self.book_storage.append(new_book)
        new_book.set_availability(True)

    def remove_book(self, book):
        self.book_storage.remove(book)
        book.set_availability(False)

    def get_book_storage(self):
        return self.book_storage

    def get_available_books(self):
        available_books = []

        for book in self.book_storage:
            if book.get_availability() is True:
                available_books.append(book)

        return available_books
    
    def get_genres(self):
        genres = set()
        for book in self.book_storage:
            genres.add(book.genre)
        return sorted(genres)
    
    def find_books_by_genre(self,genre):
        sorted_books = []
        for book in self.book_storage:
            if book.genre.lower() == genre.lower() and book.get_availability():
                sorted_books.append(book)
        return sorted_books
