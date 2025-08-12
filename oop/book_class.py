class Book:
    #Initializer for the book instance
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    #destructor called when an object is about to be destroyed
    def __del__(self):
        print(f"Deleting {self.title}")
    #sring representation
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    #official representation that recreates the instance
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"