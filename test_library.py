# ==========================================
# NEXORA - LIBRARY MANAGEMENT SYSTEM
# Automated Tests
# Developer: Innocent Kelvin
# ==========================================

import unittest

from book import Book
from library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book = Book(
            "B001",
            "Things Fall Apart",
            "Chinua Achebe"
        )
        self.library.add_book(self.book)

    # Test adding a book
    def test_add_book(self):
        self.assertEqual(len(self.library.books), 1)

    # Test preventing duplicate book IDs
    def test_duplicate_book_id(self):
        another_book = Book(
            "B001",
            "The Trial",
            "Franz Kafka"
        )
        self.library.add_book(another_book)
        self.assertEqual(len(self.library.books), 1)

    # Test searching by book ID
    def test_search_by_id(self):
        result = self.library.search_by_id("B001")
        self.assertIsNotNone(result)

    # Test searching by title
    def test_search_by_title(self):
        result = self.library.search_by_title("Things Fall Apart")
        self.assertIsNotNone(result)

    # Test borrowing an available book
    def test_borrow_book(self):
        self.library.borrow_book("B001")
        self.assertFalse(self.book.is_available)

    # Test returning a borrowed book
    def test_return_book(self):
        self.library.borrow_book("B001")
        self.library.return_book("B001")
    # Test searching for a book that does not exist
    def test_search_missing_book(self):
        result = self.library.search_by_id("B999")
        self.assertIsNone(result)

    # Test preventing a second borrowing
    def test_borrow_already_borrowed_book(self):
        self.library.borrow_book("B001")
        self.library.borrow_book("B001")
        self.assertFalse(self.book.is_available)

    # Test preventing return of a book that is not borrowed
    def test_return_available_book(self):
        self.library.return_book("B001")
        self.assertTrue(self.book.is_available)

    # Test that a book becomes available after being returned
    def test_book_availability_after_return(self):
        self.library.borrow_book("B001")
        self.library.return_book("B001")
        self.assertTrue(self.book.is_available)
        self.assertTrue(self.book.is_available)

if __name__ == "__main__":
    unittest.main()
    unittest.main()