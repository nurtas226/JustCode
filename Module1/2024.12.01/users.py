class User:

    def __init__(self, name):
        self.name = name
        self.books = []

    def take_book(self, book):
        self.books.append(book)
        book.set_availability(False)

    def return_book(self, book):
        self.books.remove(book)
        book.set_availability(True)

    def get_books(self):
        return self.books
    
    def get_taken_books(self):
        taken_books = []

        for book in self.books:
            if book.get_availability() is False:
                taken_books.append(book)

        return taken_books
    
    
   
    