# Library Directory & Search System
# Using BST, Linked List, File Handling and Exceptions


# Book Node for Linked List
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.next = None


# BST Node
class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


# Insert book into BST
def insert(root, book):

    if root is None:
        return BSTNode(book)

    if book.title.lower() < root.book.title.lower():
        root.left = insert(root.left, book)

    else:
        root.right = insert(root.right, book)

    return root


# Search book using BST
def search(root, title):

    if root is None:
        return None

    if title.lower() == root.book.title.lower():
        return root.book

    elif title.lower() < root.book.title.lower():
        return search(root.left, title)

    else:
        return search(root.right, title)


# Display books using inorder traversal
def display_catalog(root):

    if root:
        display_catalog(root.left)

        print(
            "Title:",
            root.book.title,
            "| Author:",
            root.book.author
        )

        display_catalog(root.right)


# Load catalog from file
def load_catalog(filename):

    root = None

    try:

        with open(filename, "r") as file:

            for line in file:

                title, author = line.strip().split("|")

                book = Book(title, author)

                root = insert(root, book)


    except FileNotFoundError:

        print("No catalog file found. Starting empty library.")

    return root



# Save new book to file
def add_book(filename):

    title = input("Enter book title: ")
    author = input("Enter author: ")

    try:

        with open(filename, "a") as file:

            file.write(title + "|" + author + "\n")

        print("Book added successfully")

    except Exception as e:

        print("Error:", e)



# Main Program

catalog = load_catalog("library.txt")


while True:

    print("\n===== Library Directory =====")
    print("1. Search Book")
    print("2. Display All Books")
    print("3. Add New Book")
    print("4. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        title = input("Enter book title: ")

        result = search(catalog, title)

        if result:
            print("\nBook Found")
            print("Title:", result.title)
            print("Author:", result.author)

        else:
            print("Book not found")


    elif choice == "2":

        print("\nLibrary Catalog")
        display_catalog(catalog)


    elif choice == "3":

        add_book("library.txt")

        catalog = load_catalog("library.txt")


    elif choice == "4":

        print("Program Closed")
        break


    else:

        print("Invalid option")