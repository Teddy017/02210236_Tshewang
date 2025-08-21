<<<<<<< HEAD
import json
import os

JSON_FILE = "books.json"

def initialize_json():
    """Create the JSON file if it doesn't exist"""
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as f:
            json.dump({"books": []}, f, indent=4)

def load_json():
    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    return data

def save_json(data):
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

def list_books():
    data = load_json()
    if not data["books"]:
        print("No books found.")
        return
    print("\n📚 List of Books:")
    for book in data["books"]:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

def add_book():
    data = load_json()
    book_id = input("Enter Book ID: ")

    # check if ID already exists
    for book in data["books"]:
        if str(book["id"]) == book_id:
            print("❌ Book ID already exists!")
            return

    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year: ")

    new_book = {
        "id": int(book_id),
        "title": title,
        "author": author,
        "year": int(year)
    }

    data["books"].append(new_book)
    save_json(data)
    print("✅ Book added.")

def edit_book():
    data = load_json()
    book_id = input("Enter Book ID to edit: ")

    for book in data["books"]:
        if str(book["id"]) == book_id:
            print("Press Enter to keep current value.")
            book["title"] = input(f"New Title [{book['title']}]: ") or book["title"]
            book["author"] = input(f"New Author [{book['author']}]: ") or book["author"]
            year_input = input(f"New Year [{book['year']}]: ")
            book["year"] = int(year_input) if year_input else book["year"]
            save_json(data)
            print("✅ Book updated.")
            return
    print("❌ Book not found.")

def delete_book():
    data = load_json()
    book_id = input("Enter Book ID to delete: ")

    for book in data["books"]:
        if str(book["id"]) == book_id:
            data["books"].remove(book)
            save_json(data)
            print("✅ Book deleted.")
            return
    print("❌ Book not found.")

def menu():
    while True:
        print("\nBook Library Menu")
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
    initialize_json()
    menu()
=======
import json
import os

JSON_FILE = "books.json"

def initialize_json():
    """Create the JSON file if it doesn't exist"""
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as f:
            json.dump({"books": []}, f, indent=4)

def load_json():
    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    return data

def save_json(data):
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

def list_books():
    data = load_json()
    if not data["books"]:
        print("No books found.")
        return
    print("\n📚 List of Books:")
    for book in data["books"]:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

def add_book():
    data = load_json()
    book_id = input("Enter Book ID: ")

    # check if ID already exists
    for book in data["books"]:
        if str(book["id"]) == book_id:
            print("❌ Book ID already exists!")
            return

    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year: ")

    new_book = {
        "id": int(book_id),
        "title": title,
        "author": author,
        "year": int(year)
    }

    data["books"].append(new_book)
    save_json(data)
    print("✅ Book added.")

def edit_book():
    data = load_json()
    book_id = input("Enter Book ID to edit: ")

    for book in data["books"]:
        if str(book["id"]) == book_id:
            print("Press Enter to keep current value.")
            book["title"] = input(f"New Title [{book['title']}]: ") or book["title"]
            book["author"] = input(f"New Author [{book['author']}]: ") or book["author"]
            year_input = input(f"New Year [{book['year']}]: ")
            book["year"] = int(year_input) if year_input else book["year"]
            save_json(data)
            print("✅ Book updated.")
            return
    print("❌ Book not found.")

def delete_book():
    data = load_json()
    book_id = input("Enter Book ID to delete: ")

    for book in data["books"]:
        if str(book["id"]) == book_id:
            data["books"].remove(book)
            save_json(data)
            print("✅ Book deleted.")
            return
    print("❌ Book not found.")

def menu():
    while True:
        print("\nBook Library Menu")
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
    initialize_json()
    menu()
>>>>>>> ee95f4148d8ac7ac34a7b07332c3144224aaccc0
