# -*- coding: utf-8 -*-

"""
White-box unit testing part 3.
"""
import unittest
from unittest.mock import patch

from book_store import (
    Book, 
    BookStore
)

class TestBook(unittest.TestCase):
    """
    """

    def setUp(self):
        self.book = Book("Java", "Alan", 20, 5)

    def test_initialize_book(self):
        """
        """
        self.assertEqual(self.book.title, "Java")
        self.assertEqual(self.book.author, "Alan")
        self.assertEqual(self.book.price, 20)
        self.assertEqual(self.book.quantity, 5)

    @patch("builtins.print")
    def test_display_book(self, mock_print):
        """
        """
        self.book.display()
        mock_print.assert_any_call(f"Title: {self.book.title}")
        mock_print.assert_any_call(f"Author: {self.book.author}")
        mock_print.assert_any_call(f"Price: ${self.book.price}")
        mock_print.assert_any_call(f"Quantity: {self.book.quantity}")


class TestBookStore(unittest.TestCase):

    def setUp(self):
        self.store = BookStore()
        self.book = Book("Java", "Alan", 20, 5)

    def test_initialize_store(self):
        """
        """
        self.assertEqual(self.store.books, [])

    @patch("builtins.print")
    def test_add_book(self, mock_print):
        """
        """
        self.store.add_book(self.book)
        self.assertEqual(len(self.store.books), 1)
        mock_print.assert_called_with(
            f"Book '{self.book.title}' added to the store."
        )

    @patch("builtins.print")
    def test_display_no_books(self, mock_print):
        """
        """
        self.store.display_books()
        mock_print.assert_called_with("No books in the store.")

    @patch("builtins.print")
    def test_display_books_with_books(self, mock_print):
        """
        """
        self.store.add_book(self.book)
        self.store.display_books()
        mock_print.assert_any_call("Books available in the store:")

    @patch("builtins.print")
    def test_search_book_found(self, mock_print):
        """
        """
        self.store.add_book(self.book)
        self.store.search_book("Java")
        mock_print.assert_any_call(
            "Found 1 book(s) with title 'Java':"
        )

    @patch("builtins.print")
    def test_search_book_not_found(self, mock_print):
        self.store.search_book("Java")
        mock_print.assert_called_with(
            "No book found with title 'Java'."
    )