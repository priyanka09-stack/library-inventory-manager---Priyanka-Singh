import json
from pathlib import Path
from library_manager.book import Book
import logging

# Setup logging
logging.basicConfig(filename="library.log", level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

class LibraryInventory:
    def __init__(self, file_path="books.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()
        logging.info(f"Book added: {book.title}")

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        return [book for book in self.books if book.isbn == isbn]

    def display_all(self):
        return self.books

    def save_books(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump([book.to_dict() for book in self.books], f, indent=4)
        except Exception as e:
            logging.error(f"Error saving books: {e}")

    def load_books(self):
        if not self.file_path.exists():
            return
        try:
            with open(self.file_path, "r") as f:
                book_list = json.load(f)
                self.books = [Book(**b) for b in book_list]
        except Exception as e:
            logging.error(f"Error loading books: {e}")
