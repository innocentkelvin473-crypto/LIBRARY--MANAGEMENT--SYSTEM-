# NEXORA - LIBRARY MANAGEMENT SYSTEM
# Library Class
# Developer: Innocent Kelvin



# Import the Book class
from book import Book


# Define the Library class
class Library:

    # Initialise an empty library
    def __init__(self):
        self.books = []

    # Add a book to the library
    def add_book(self, book):

        # Check whether the book ID already exists
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print("Book ID already exists")
                return

        # Add the book if the ID is unique
        self.books.append(book)
        print("Book successfully added")

    # Display all books in the library
    def display_books(self):

        if not self.books:
            print("No books found in the library")
            return

        for book in self.books:

            availability = "Available" if book.is_available else "Borrowed"

            print("----------------------------")
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Availability:", availability)

    # Search for a book using its ID
    def search_by_id(self, book_id):

        for book in self.books:
            if book.book_id == book_id:
                print("Book found")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Availability:", book.is_available)
                return book

        print("Book not found")
        return None

    # Search for a book using its title
    def search_by_title(self, title):

        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book found")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Availability:", book.is_available)
                return book

        print("Book not found")
        return None

    # Borrow a book using its ID
    def borrow_book(self, book_id):

        for book in self.books:
            if book.book_id == book_id:

                if book.is_available:
                    book.is_available = False
                    print("Book successfully borrowed")
                else:
                    print("Book is already borrowed")

                return

        print("Book not found")

    # Return a borrowed book using its ID
    def return_book(self, book_id):

        for book in self.books:
            if book.book_id == book_id:

                if not book.is_available:
                    book.is_available = True
                    print("Book successfully returned")
                else:
                    print("Book has not been borrowed")

                return

        print("Book not found")
