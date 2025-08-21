import xml.etree.ElementTree as ET
import os

XML_FILE = 'book.xml'

# Create XML file if it doesn't exist
def create_xml():
    if not os.path.exists(XML_FILE):
        root = ET.Element('library')
        tree = ET.ElementTree(root)
        tree.write(XML_FILE)

# Load XML
def load_xml():
    tree = ET.parse(XML_FILE)
    return tree, tree.getroot()

# List all books
def list_books():
    _, root = load_xml()
    books = root.findall('book')
    if not books:
        print("No books found.")
    for book in books:
        print(f"{book.attrib['id']} - {book.find('title').text} by {book.find('author').text} ({book.find('year').text})")

# Add a new book
def add_book():
    book_id = input("Enter ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year: ")

    tree, root = load_xml()
    if root.find(f"./book[@id='{book_id}']"):
        print("Book ID already exists.")
        return

    new_book = ET.Element('book', id=book_id)
    ET.SubElement(new_book, 'title').text = title
    ET.SubElement(new_book, 'author').text = author
    ET.SubElement(new_book, 'year').text = year
    root.append(new_book)
    tree.write(XML_FILE)
    print("Book added!")

#edit a book
def edit_book():
    book_id = input("Enter Book ID to edit: ")
    tree, root = load_xml()
    book = root.find(f"./book[@id='{book_id}']")
    if book is None:
        print("Book not found.")
        return
    print("Press Enter to keep current value.")
    new_title = input(f"New Title [{book.find('title').text}]: ") or book.find('title').text
    new_author = input(f"New Author [{book.find('author').text}]: ") or book.find('author').text
    new_year = input(f"New Year [{book.find('year').text}]: ") or book.find('year').text
    book.find('title').text = new_title
    book.find('author').text = new_author
    book.find('year').text = new_year
    tree.write(XML_FILE)
    print("Book updated.")

# Delete a book
def delete_book():
    book_id = input("Enter ID to delete: ")
    tree, root = load_xml()
    book = root.find(f"./book[@id='{book_id}']")
    if book is not None:
        root.remove(book)
        tree.write(XML_FILE)
        print("Book deleted.")
    else:
        print("Book not found.")

# Menu
def menu():
    while True:
        print("\n1. List Books\n2. Add Book\n3. Edit Book\n4. Delete Book\n5. Exit")
        choice = input("Choose: ")

        if choice == '1':
            list_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            edit_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

# Run program
if __name__ == "__main__":
    create_xml()
    menu()
