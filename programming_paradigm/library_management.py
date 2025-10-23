class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added.")

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                return f"'{book.title}' has been checked out."
        return f"Book '{title}' is not available."

    def return_book(self, title):
        """Return a book by title if it was checked out."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    return f"'{book.title}' has been returned."
                else:
                    return f"Book '{title}' was not checked out."
        return f"Book '{title}' not found in the library."

    def list_available_books(self):
        """List all available books in the library."""
        available = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
        return available if available else ["No books available."]


