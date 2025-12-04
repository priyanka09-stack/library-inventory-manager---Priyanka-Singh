import unittest
from library_manager.book import Book
from library_manager.inventory import LibraryInventory

class TestLibrary(unittest.TestCase):
    def test_book_issue_return(self):
        b = Book("Test", "Author", "123")
        self.assertTrue(b.is_available())
        b.issue()
        self.assertFalse(b.is_available())
        b.return_book()
        self.assertTrue(b.is_available())

    def test_inventory_add_search(self):
        inv = LibraryInventory(file_path="test_books.json")
        b = Book("Test2", "Author2", "456")
        inv.add_book(b)
        self.assertEqual(len(inv.search_by_title("Test2")), 1)
        inv.save_books()

if __name__ == "__main__":
    unittest.main()

