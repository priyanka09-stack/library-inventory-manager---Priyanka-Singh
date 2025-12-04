from library_manager.inventory import LibraryInventory
from library_manager.book import Book
import logging

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

inventory = LibraryInventory()

def menu():
    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        try:
            if choice == "1":
                title = input("Enter title: ").strip()
                author = input("Enter author: ").strip()
                isbn = input("Enter ISBN: ").strip()
                inventory.add_book(Book(title, author, isbn))
                print("Book added successfully.")
            elif choice == "2":
                isbn = input("Enter ISBN to issue: ").strip()
                books = inventory.search_by_isbn(isbn)
                if books:
                    books[0].issue()
                    inventory.save_books()
                    print(f"Book '{books[0].title}' issued successfully.")
                else:
                    print("Book not found.")
            elif choice == "3":
                isbn = input("Enter ISBN to return: ").strip()
                books = inventory.search_by_isbn(isbn)
                if books:
                    books[0].return_book()
                    inventory.save_books()
                    print(f"Book '{books[0].title}' returned successfully.")
                else:
                    print("Book not found.")
            elif choice == "4":
                inventory.display_all()
            elif choice == "5":
                term = input("Enter title or ISBN to search: ").strip()
                results = inventory.search_by_title(term) + inventory.search_by_isbn(term)
                if results:
                    for b in results:
                        print(b)
                else:
                    print("No matching books found.")
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please enter 1-6.")
        except Exception as e:
            print(f"Error: {e}")
            logging.error(f"Exception: {e}")

if __name__ == "__main__":
    menu()
