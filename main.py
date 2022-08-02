import users
import books

print('')
print(f'Welcome to Simple Library.')

def main_menu():
    print('')
    print('-----------------------------------------------')
    print('            Simple Library main menu'           )
    print('-----------------------------------------------')
    print('')
    print('[ 1 ] Register new user') 
    print('[ 2 ] Show user database') 
    print('[ 3 ] Book menu') 
    print('[ 0 ] Exit Simple Library') 
    print('')
    print('-----------------------------------------------')
    print('')

def book_menu():
    print('')
    print('-----------------------------------------------')
    print('           Simple Library book menu'            )
    print('-----------------------------------------------')
    print('')
    print('[ 1 ] Register new book') 
    print('[ 2 ] Show book database') 
    print('[ 3 ] Search book')
    print('[ 4 ] Rent a book') 
    print('[ 5 ] Return a book') 
    print('[ 6 ] Show rent database') 
    print('[ 0 ] Back to main menu') 
    print('')
    print('-----------------------------------------------')
    print('')

main_menu()
user_option = input('Insert your option: ')
numbers = [str(number) for number in range (10)]
while user_option not in numbers: # To defend input from character other than numbers
    print('')
    print('Invalid operation')
    main_menu()
    user_option = input('Insert your option: ')

while user_option != '0':
    
    if user_option == '1':
        users.register()
    elif user_option == '2':
        users.fetch_database()
    elif user_option == '3':
        book_menu()
        user_option = input('Insert your option: ')
        numbers = [str(number) for number in range (10)]
        while user_option not in numbers: # To defend input from character other than numbers
            print('')
            print('Invalid operation')
            book_menu()
            user_option = input('Insert your option: ')
            
        while user_option != '0':
            if user_option == '1':
                books.register()
            elif user_option == '2':
                books.fetch_database()
            elif user_option == '3':
                try:
                    search_result = books.db_con.pd.DataFrame(books.search())
                    search_result.columns = books.db_con.mycursor.column_names
                    print('Search result: ')
                    print('')
                    print(search_result)
                    print('')
                    input('Press any key to return to book menu: ')
                except:
                    pass
            elif user_option == '4':
                books.rent()
            elif user_option == '5':
                books.return_book()
            elif user_option == '6':
                books.fetch_rent_database()
            else:
                print('Invalid operation')

            book_menu()
            user_option = input('Insert your option: ')
            numbers = [str(number) for number in range (10)]
            while user_option not in numbers:
                print('')
                print('Invalid operation')
                book_menu()
                user_option = int(input('Insert your option: '))
    else:
        print('Invalid operation')

    main_menu()
    user_option = input('Insert your option: ')
    numbers = [str(number) for number in range (10)]
    while user_option not in numbers:
        print('')
        print('Invalid operation')
        main_menu()
        user_option = input('Insert your option: ')

print('Thanks for using Simple Library goodbye!')

books.db_con.mycursor.close()
users.db_con.mycursor.close()
books.db_con.db.close()
users.db_con.db.close()