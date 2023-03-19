

def save_book_to_the_file(book_data):
    try:
        fileobj =open("books.txt", 'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.write(book_data)
        fileobj.close()
        return True

def get_all_books_from_file():
    try:
        fileobj =open("books.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        books = fileobj.readlines()
        return books


def find_book_by_id(book_id):
    books = get_all_books_from_file()
    for book in books:
        # if str(book_id) in book:
        #     return True, book
        print(book)
        book_details = book.strip('\n').split(":")  # list book_details
        if book_details[0]==str(book_id):
            return True , book
    else:
        return False


def save_books_to_file(listofbooks):
    try:
        fileobj =open("books.txt", 'w')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(listofbooks)
        fileobj.close()
        return True


def delete_book_from_file(book):
    books= get_all_books_from_file()
    books.remove(book)  # list
    removed = save_books_to_file(books)
    return removed