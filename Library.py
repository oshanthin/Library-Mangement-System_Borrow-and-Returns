from datetime import datetime


LIBRARY_FILE = "library.txt"
BORROW_FILE = "borrow_log.txt"


# ---------------- Get Book Details ----------------

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



# ---------------- Borrow Book ----------------

def borrow(book_id, student_id):

    book = get_book(book_id)


    if book is None:

        print("Book not found")
        return



    # Check whether book is already borrowed

    try:

        file = open(BORROW_FILE, "r")


        for line in file:

            data = line.strip().split("|")


            if (
                data[0] == str(book_id)
                and data[2] == "BORROWED"
            ):

                file.close()

                raise ValueError(
                    "Book already on loan"
                )


        file.close()


    except FileNotFoundError:

        # First borrow, file does not exist
        pass



    # Add borrow record

    file = open(BORROW_FILE, "a")


    borrow_date = datetime.now().strftime(
        "%Y-%m-%d"
    )


    file.write(
        f"{book_id}|{student_id}|BORROWED|{borrow_date}\n"
    )


    file.close()



    print("\nBook Borrowed Successfully")
    print("---------------------------")
    print("Book ID :", book["id"])
    print("Title   :", book["title"])
    print("Author  :", book["author"])
    print("Student :", student_id)



# ---------------- Return Book ----------------

def return_book(book_id):


    try:

        file = open(BORROW_FILE, "r")


        records = file.readlines()


        file.close()



    except FileNotFoundError:

        print("No borrow records found")

        return



    updated_records = []

    returned = False



    for record in records:


        data = record.strip().split("|")



        if (
            data[0] == str(book_id)
            and data[2] == "BORROWED"
        ):


            data[2] = "RETURNED"


            data.append(
                datetime.now().strftime("%Y-%m-%d")
            )


            returned = True



        updated_records.append(
            "|".join(data)
        )



    file = open(BORROW_FILE, "w")


    for record in updated_records:

        file.write(record + "\n")


    file.close()



    if returned:

        print("Book returned successfully")

    else:

        print(
            "Book not found or already returned"
        )



# ---------------- Display Books ----------------

def display_books():


    file = open(LIBRARY_FILE, "r")


    print("\nLibrary Books")
    print("-----------------------")


    for line in file:


        data = line.strip().split("|")


        print(
            "ID:",
            data[0],
            "| Title:",
            data[1],
            "| Author:",
            data[2]
        )


    file.close()



# ---------------- View Borrow Log ----------------

def view_borrow_log():


    try:

        file = open(BORROW_FILE, "r")


        print("\nBorrow Log")
        print("-----------------------")


        for line in file:

            print(line.strip())


        file.close()



    except FileNotFoundError:

        print("No borrow records")



# ---------------- Main Program ----------------


while True:


    print("\n===== Library Management System =====")

    print("1. View Books")

    print("2. Borrow Book")

    print("3. Return Book")

    print("4. View Borrow Log")

    print("5. Exit")



    choice = input(
        "Enter your choice: "
    )



    if choice == "1":

        display_books()



    elif choice == "2":


        book_id = input(
            "Enter Book ID: "
        )


        student_id = input(
            "Enter Student ID: "
        )



        try:

            borrow(
                book_id,
                student_id
            )


        except ValueError as e:

            print(
                "Error:",
                e
            )



    elif choice == "3":


        book_id = input(
            "Enter Book ID to return: "
        )


        return_book(book_id)



    elif choice == "4":

        view_borrow_log()



    elif choice == "5":

        print(
            "Thank you!"
        )

        break



    else:

        print(
            "Invalid choice"
        )