
# NEXORA - LIBRARY MANAGEMENT SYSTEM
# Book Class
# Developer: Innocent Kelvin


# Define the Book class
class Book:

    # Initialise a new book
    def __init__(self, book_id, title, author):

        # Book attributes
        self.book_id = book_id
        self.title = title
        self.author = author

        # Every new book is available by default
        self.is_available = True
