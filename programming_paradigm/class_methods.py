class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total books created: {cls.total_books}")

b1 = Book("Python 101")
b2 = Book("Learn OOP")
b3 = Book("Cybersecurity Basics") 

Book.display_total_books()