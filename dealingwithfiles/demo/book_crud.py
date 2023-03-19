from inputshelper import  askforstring, askforInt, generate_id
from filehandler import  save_book_to_the_file, get_all_books_from_file, \
    find_book_by_id, delete_book_from_file

def create_book():
    ## ask for title , no_of_pages
    title = askforstring("Please enter book title: ")
    no_of_pages = askforInt("Please enter no of pages: ")
    print(title, no_of_pages)

    book_id = generate_id()
    book_data = f"{book_id}:{title}:{no_of_pages}\n"
    added = save_book_to_the_file(book_data)
    if added:
        print("---book added successfully---")
    else:
        print("=== problem happended ---> try again please ----")



def display_all_books():
    books = get_all_books_from_file()
    if books:
        print(books)
        for book in books:
            print(book)
    else:
        print('---- Error happened please try again ----')

def delete_book():
    book_id = askforInt("Please enter the id of the book you want to delete: ") # int
    ## search if book exists in the books
    found = find_book_by_id(book_id)
    if found :
        print("--- book found ")
        removed=delete_book_from_file(found[1])
        if removed:
            print('--- book deleted successfully ---')
        else:
            print("--- problem happened while deleting the book ---")
    else:
        print("Book not found, please try again with valid id ")
    ## delete ?
