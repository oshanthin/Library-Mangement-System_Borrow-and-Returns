from datetime import datetime


LIBRARY_FILE = "library.txt"
BORROW_FILE = "borrow_log.txt"


# Get book details from library.txt
def get_book(book_id):

    file = open(LIBRARY_FILE, "r")

    for line in file:

        data = line.strip().split("|")

        if data[0] == str(book_id):

            file.close()

            return {
                "id": data[0],
                "title": data[1],
                "author": data[2]
            }

    file.close()

    return None



# Borrow book
def borrow(book_id, student_id):

    book = get_book(book_id)


    if book is None:

        print("Book not found")
        return



    # Check existing borrow records

    file = open(BORROW_FILE, "r")


    for line in file:

        data = line.strip().split("|")


        if data[0] == str(book_id) and data[2] == "BORROWED":

            file.close()

            raise ValueError(
                "Book is unavailable for borrowing. It has already been borrowed."
            )


    file.close()



    # Add new record

    file = open(BORROW_FILE, "a")


    date = datetime.now().strftime("%Y-%m-%d")


    file.write(
        f"{book_id}|{student_id}|BORROWED|{date}\n"
    )


    file.close()



    print("\nBook Borrowed Successfully")
    print("---------------------------")
    print("Book ID :", book["id"])
    print("Title   :", book["title"])
    print("Author  :", book["author"])



# Return book
def return_book(book_id):

    file = open(BORROW_FILE, "r")


    records = file.readlines()


    file.close()


    updated_records = []

    found = False



    for record in records:

        data = record.strip().split("|")


        if data[0] == str(book_id) and data[2] == "BORROWED":


            data[2] = "RETURNED"

            data.append(
                datetime.now().strftime("%Y-%m-%d")
            )

            found = True



        updated_records.append(
            "|".join(data)
        )



    file = open(BORROW_FILE, "w")


    for record in updated_records:

        file.write(record + "\n")


    file.close()



    if found:

        print("Book returned successfully")

    else:

        print("Book not found")



# Display books
def display_books():

    file = open(LIBRARY_FILE, "r")


    print("\nLibrary Books")
    print("----------------")


    for line in file:

        data = line.strip().split("|")


        print(
            "ID:",
            data[0],
            "Title:",
            data[1],
            "Author:",
            data[2]
        )


    file.close()



# Main Program

while True:

    print("\n1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")


    choice = input("Enter choice: ")



    if choice == "1":

        display_books()



    elif choice == "2":

        book_id = input("Enter Book ID: ")

        student_id = input("Enter Student ID: ")


        try:

            borrow(
                book_id,
                student_id
            )

        except ValueError as e:

            print(e)



    elif choice == "3":

        book_id = input(
            "Enter Book ID: "
        )

        return_book(book_id)



    elif choice == "4":

        break


    else:

        print("Invalid choice")