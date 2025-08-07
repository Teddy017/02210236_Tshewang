import xml.etree.ElementTree as ET
import os

XML_FILE = 'book.xml'

def initialize_xml():
    """Create the XML file if it doesn't exist"""
    if not os.path.exists(XML_FILE):
        root = ET.Element('library')
        tree = ET.ElementTree(root)
        tree.write(XML_FILE)

def load_xml():
    tree = ET.parse(XML_FILE)
    return tree, tree.getroot()

def list_books():
    tree, root = load_xml()
    if not root.findall('book'):
        print("No books found.")
        return
    print("\n📚 List of Books:")
    for book in root.findall('book'):
        print(f"ID: {book.attrib['id']}, Title: {book.find('title').text}, "
              f"Author: {book.find('author').text}, Year: {book.find('year').text}")

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year: ")
    tree, root = load_xml()
    if root.find(f"./book[@id='{book_id}']") is not None:
        print("❌ Book ID already exists!")
        return
    new_book = ET.Element('book', id=book_id)
    ET.SubElement(new_book, 'title').text = title
    ET.SubElement(new_book, 'author').text = author
    ET.SubElement(new_book, 'year').text = year
    root.append(new_book)
    tree.write(XML_FILE)
    print("✅ Book added.")

def edit_book():
    book_id = input("Enter Book ID to edit: ")
    tree, root = load_xml()
    book = root.find(f"./book[@id='{book_id}']")
    if book is None:
        print("❌ Book not found.")
        return
    print("Press Enter to keep current value.")
    new_title = input(f"New Title [{book.find('title').text}]: ") or book.find('title').text
    new_author = input(f"New Author [{book.find('author').text}]: ") or book.find('author').text
    new_year = input(f"New Year [{book.find('year').text}]: ") or book.find('year').text
    book.find('title').text = new_title
    book.find('author').text = new_author
    book.find('year').text = new_year
    tree.write(XML_FILE)
    print("✅ Book updated.")

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    tree, root = load_xml()
    book = root.find(f"./book[@id='{book_id}']")
    if book is not None:
        root.remove(book)
        tree.write(XML_FILE)
        print("✅ Book deleted.")
    else:
        print("❌ Book not found.")

def menu():
    while True:
        print("\n📖 Book Library Menu")
        print("1. List all books")
        print("2. Add a new book")
        print("3. Edit a book")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            list_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            edit_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    initialize_xml()
    menu()
