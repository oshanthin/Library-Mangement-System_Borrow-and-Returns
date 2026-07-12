"""
Team 1 - Borrow & Return
Records which book each student holds, and processes returns permanently
using a sequential text file (borrow_log.txt).

File format (one loan record per line):
    book_id,student_id,status
where status is either "ON_LOAN" or "RETURNED"
"""

LOG_FILE = "borrow_log.txt"


def borrow(book_id, student_id):
    """
    Append a new borrow record to borrow_log.txt.
    Raises ValueError if the book is already on loan.
    """
    # check existing records first
    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                existing_book_id, existing_student_id, status = parts
                if existing_book_id == book_id and status == "ON_LOAN":
                    raise ValueError(f"Book {book_id} is already on loan.")
    except FileNotFoundError:
        # no log file yet means no books have been borrowed
        pass

    # append new borrow record
    with open(LOG_FILE, "a") as file:
        file.write(f"{book_id},{student_id},ON_LOAN\n")


def return_book(book_id):
    """
    Update borrow_log.txt to mark the book as returned (frees the book).
    Raises ValueError if there is no active loan for the book.
    """
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise ValueError(f"No loan record found for book {book_id}.")

    updated_lines = []
    found = False

    for line in lines:
        parts = line.strip().split(",")
        if len(parts) != 3:
            continue
        existing_book_id, student_id, status = parts

        if existing_book_id == book_id and status == "ON_LOAN":
            updated_lines.append(f"{book_id},{student_id},RETURNED\n")
            found = True
        else:
            updated_lines.append(line if line.endswith("\n") else line + "\n")

    if not found:
        raise ValueError(f"No active loan found for book {book_id}.")

    with open(LOG_FILE, "w") as file:
        file.writelines(updated_lines)


# simple test run
if __name__ == "__main__":
    borrow("B101", "S001")
    print("Borrowed B101 for S001")

    try:
        borrow("B101", "S002")
    except ValueError as e:
        print("Expected error:", e)

    return_book("B101")
    print("Returned B101")

    # should be borrowable again now
    borrow("B101", "S002")
    print("Borrowed B101 for S002")