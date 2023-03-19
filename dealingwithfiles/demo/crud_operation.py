

#### console application ---> save info about books
from book_crud import create_book,display_all_books, delete_book

def mainmenu():
    while True:
        choice = input("please enter n for new , l for list all , e for edit , d for delete, x for exit: ")
        if choice=='n':
            create_book()
        elif choice=='l':
            display_all_books()
        elif choice=='e':
            pass
        elif choice=='d':
            delete_book()
        elif choice=='x':
            print("====> Bye <====")
            exit()

mainmenu()