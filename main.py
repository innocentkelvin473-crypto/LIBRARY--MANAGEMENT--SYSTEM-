
# ==========================================
# NEXORA - LIBRARY MANAGEMENT SYSTEM
# Main Application
# Developer: Innocent Kelvin
# ==========================================

# Import required classes
from book import Book
from library import Library


# Create a library object
my_library = Library()


# ==========================================
# 1. ADD BOOKS
# ==========================================

print("\nADDING BOOKS")

book1 = Book("B001", "Things Fall Apart", "Chinua Achebe")
book2 = Book("B002", "The River Between", "Ngugi wa Thiong'o")
book3 = Book("B001", "The Trial", "Franz Kafka")

my_library.add_book(book1)
my_library.add_book(book2)

# Attempt to add a duplicate book ID
my_library.add_book(book3)


# ==========================================
# 2. DISPLAY ALL BOOKS
# ==========================================

print("\nLIBRARY BOOK COLLECTION")
my_library.display_books()


# ==========================================
# 3. SEARCH BOOKS BY ID
# ==========================================

print("\nSEARCHING BY BOOK ID")
my_library.search_by_id("B001")

print("\nSEARCHING FOR MISSING BOOK")
my_library.search_by_id("B005")


# ==========================================
# 4. SEARCH BOOKS BY TITLE
# ==========================================

print("\nSEARCHING BY TITLE")
my_library.search_by_title("Things Fall Apart")

print("\nSEARCHING FOR MISSING TITLE")
my_library.search_by_title("The Lost World")


# ==========================================
# 5. BORROW BOOKS
# ==========================================

print("\nBORROWING A BOOK")
my_library.borrow_book("B001")

print("\nBORROWING THE SAME BOOK AGAIN")
my_library.borrow_book("B001")


# ==========================================
# 6. RETURN BOOKS
# ==========================================

print("\nRETURNING A BOOK")
my_library.return_book("B001")

print("\nATTEMPTING TO RETURN THE SAME BOOK AGAIN")
my_library.return_book("B001")


# ==========================================
# 7. DISPLAY FINAL BOOK COLLECTION
# ==========================================

print("\nFINAL LIBRARY COLLECTION")
my_library.display_books()
