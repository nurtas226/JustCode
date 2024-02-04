class Book:

    def __init__(self, title, author,genre):
        self.title = title
        self.author = author
        self.genre = genre
        
        self.is_available = False

    def __repr__(self):
        return f'"{self.title}" {self.author}'

    def set_availability(self, is_available):
        self.is_available = is_available

    def get_availability(self):
        return self.is_available