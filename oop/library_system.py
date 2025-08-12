#Base class
class Book:
    def  __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

  #Derived class Ebook      
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author) #calls the base constructor
        self.file_size = file_size

    def __str__(self):
        return  f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
    
    #Derived class PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

        
# Composition: Library
class Library:
    def __init__(self):
        self.books = []  # List to store any type of Book

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
           
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(f"{book}")
    