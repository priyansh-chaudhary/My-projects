class Book :
    def __init__(self, title, author, isbn) :
        self.title = title
        self.author = author
        self.isbn = isbn

    def getDetails(self) :
        print(f"Title : {self.title}, Author : {self.author}, ISBN : {self.isbn} ")

    @classmethod
    def fromString(cls, book) :
        title, author, isbn = book.split(", ")
        return cls(title, author, isbn)

class Library :
    def __init__(self):
        self.books = []

    def addBook(self, book) :
        self.books.append(book)

    def removeBook(self, isbn) :
        for book in self.books :
            if book.isbn == isbn :
                self.books.remove(book)
                print(f"{book.title} is removed from the Library.")
                return
        print(f"There is no book of isbn : {isbn}")

    def listBooks(self) :
        if (not self.books) :
                print("There is no book in Library.")
        else :
            for book in self.books :
                book.getDetails()

book1 = Book.fromString("The Alchemist, Paulo Coelho, 9780061122415")
book2 = Book.fromString("1984, George Orwell, 9780451524935")


library = Library()
library.addBook(book1)
library.addBook(book2)
library.removeBook("9780451524935")
library.listBooks()
