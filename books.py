import db_con

def register():
    """
    Registering new book to database.

    User input:
        book_title (str): Title of the book
        book_author (str): Book author
        book_published_year (str): Book published year
        book_stock (str): Book stock
    """
    print('')
    print('-----------------------------------------------')
    print('              Register new book'                )
    print('-----------------------------------------------')
    print('')

    book_title = input(f'Book title: ').title()
    book_author = input(f'Book author: ').title()
    book_published_year = input(f'Book published year: ')
    book_stock = input('Input book stock: ')
    print('')

    db_con.mycursor.execute(
        """
        INSERT INTO books (book_title, book_author, book_published_year, book_stock) 
        VALUES (%s,%s,%s,%s)
        """, (book_title, book_author, book_published_year, book_stock)
    )

    db_con.db.commit()

    print('Book registration success!')
    print('')
    input('Press any key to return to book menu: ')
    return ('')

def fetch_database():
    """
    Showing all book data in the database. As the database grow, the amount of the data shown will be adjusted.
    """
    print('')
    print('-----------------------------------------------')
    print('                  Book database'                )
    print('-----------------------------------------------')
    print('')
    db_con.mycursor.execute(
    """
    SELECT * FROM books;
    """
    )
    try:
        book_database = db_con.pd.DataFrame(db_con.mycursor.fetchall())
        book_database.columns = db_con.mycursor.column_names
        print(book_database)
    except:
        print('No book in the database. ')

    print('')
    input('Press any key to return to book menu: ')
    return ('')

def fetch_rent_database():
    """
    Showing all rent data in the database. As the database grow, the amount of the data shown will be adjusted.
    """
    print('')
    print('-----------------------------------------------')
    print('             Book rent database'                )
    print('-----------------------------------------------')
    print('')
    
    db_con.mycursor.execute(
        """
        SELECT *
        FROM rents
        """
    )

    try:
        book_rent_db = db_con.pd.DataFrame(db_con.mycursor.fetchall())
        book_rent_db.columns = db_con.mycursor.column_names
        print(book_rent_db)
    except:
        print('No one is borrowing books at the moment')
    print('')
    input('Press any key to return to book menu: ')
    return ('')

def search():
    """
    Search for specific book in the database and saved the search result temporarily.
    
    User input:
        book_title (str): Title of the book
        book_author (str): Book author
        book_published_year (str): Book published year
    """

    book_title = input('Book title: ').title()
    book_author = input(f'Book author: ').title()
    book_published_year = input(f'Book published year: ')

    db_con.mycursor.execute( # Searching for book in database
    """
    SELECT *
    FROM books
    WHERE book_title = (%s) AND
        book_author = (%s) AND
        book_published_year = (%s)
    """, (book_title, book_author, book_published_year)
    )
    search_result = db_con.mycursor.fetchall()

    while search_result == []:
        print('')
        print('Book not found')
        print('')

        print('[ 1 ] Input another book')
        print('[   ] Press any key to return to book menu')
        print('')
        user_input = input('Insert your option: ')

        if user_input == '1':
            print('')
            book_title = input('Book title: ').title()
            book_author = input(f'Book author: ').title()
            book_published_year = input(f'Book published year: ')

            db_con.mycursor.execute( # Searching for book in database with updated input
            """
            SELECT *
            FROM books
            WHERE book_title = (%s) AND
                book_author = (%s) AND
                book_published_year = (%s)
            """, (book_title, book_author, book_published_year)
            )
            search_result = db_con.mycursor.fetchall()
        
        else:
            return ('')

    return search_result

def rent():
    """
    Renting a book. Decreasing book stock & adding user to rent database.

    User input:
        user_name (str): User that want to rent a book
        book_title (str) (Explicitly inputted from search()) function: Title of the book
        book_author (str) (Explicitly inputted from search()): Book author
        book_published_year (str) (Explicitly inputted from search()): Book published year
    """
    print('')
    print('-----------------------------------------------')
    print('                    Rent a book'                )
    print('-----------------------------------------------')
    print('')

    user_name = input('Borrower\'s user name: ').title()

    db_con.mycursor.execute( # Fetching all user names that already rent a book
        """
        SELECT user_name
        FROM rents;
        """
    )
    rents_user_name =  db_con.mycursor.fetchall()

    list_borrower = []
    for rents_row in rents_user_name:
        list_borrower.append(rents_row[0])
    

    db_con.mycursor.execute( # Fetching all user names in users database
        """
        SELECT user_name
        FROM users;
        """
    )
    users_user_name =  db_con.mycursor.fetchall()

    list_users = []
    for users_row in users_user_name:
        list_users.append(users_row[0])

    while user_name in list_borrower or user_name not in list_users: # Checking negative cases where user name inputted is not registered or has not return a book.
        if user_name in list_borrower: 
            db_con.mycursor.execute( 
            """
            SELECT *
            FROM rents
            WHERE user_name = %s;
            """, (user_name,)
            )

            print('Sorry, this user has already rent a book.'),
            print('')
            borrowers_data = db_con.pd.DataFrame(db_con.mycursor.fetchall())
            borrowers_data.columns = db_con.mycursor.column_names
            print(borrowers_data)
        
        else:
            print('')
            print('User is not registered')
            print('')
        
        print('')
        print('[ 1 ] Enter another user name')
        print('[   ] Press any key to return to book menu')
        print('')
        user_input = input('Insert your option: ')
        
        if user_input == '1':
            print('')
            user_name = input('Borrower\'s user name: ').title()

        else:
            return ('')

    book_to_rent = search() # Checking for book availability
    while book_to_rent[0][4] == 0: # If book stock is 0
        print('')
        print('Book out of stock')
        print('')

        print('[ 1 ] Input another book')
        print('[   ] Press any key to return to book menu')
        print('')

        user_input = input('Insert your option: ')
        if user_input == '1':
            print('')
            book_to_rent = search()


    db_con.mycursor.execute( # Getting user id that matched with the inputted user name
    """
    SELECT user_id
    FROM users
    WHERE user_name = %s
    """,(user_name,)
    )

    user_id = list(db_con.mycursor.fetchone())

    book_id = book_to_rent[0][0]

    db_con.mycursor.execute( # Inserting data to rent database
    """
    INSERT INTO rents (
        user_id,
        user_name, 
        book_id,
        book_title,
        rent_date,
        return_date
    )
    VALUES (
        %s,%s,%s,%s,CURDATE(),CURDATE()+7
    )
    """, (
        user_id[0], 
        user_name, 
        book_id, 
        book_to_rent[0][1]
        )
    )

    db_con.mycursor.execute( # Updating book stock in the book database
    """
    UPDATE books 
    SET book_stock = book_stock - 1
    WHERE book_id = %s
    """,(book_to_rent[0][0],)
    )

    db_con.mycursor.execute(
    """
    SELECT book_stock
    FROM books
    WHERE book_id = %s
    """,(book_to_rent[0][0],)
    )        

    updated_stock = list(db_con.mycursor.fetchone())

    print('')
    print('Book successfuly rent!')
    print(f'Current {book_to_rent[0][1]} stock: {updated_stock[0]}')

    db_con.db.commit()
    print('')
    input('Press any key to return to book menu: ')
    return ('')

def return_book():
    """
    Returning rented book. Adding book stock and removing user from rent database.

    User input:
        user_name (str): User name that want to return a book
    """
    print('')
    print('-----------------------------------------------')
    print('                  Return a book'                )
    print('-----------------------------------------------')
    print('')
    user_name = input('Borrower\'s user name: ').title()

    db_con.mycursor.execute( # Fetching all user names that already rent a book
    """
    SELECT user_name
    FROM rents;
    """
    )
    rents_user_name =  db_con.mycursor.fetchall()

    list_borrower = []
    for rents_row in rents_user_name:
        list_borrower.append(rents_row[0])


    db_con.mycursor.execute( # Fetching all user names in users database
    """
    SELECT user_name
    FROM users;
    """
    )
    users_user_name =  db_con.mycursor.fetchall()

    list_users = []
    for users_row in users_user_name:
        list_users.append(users_row[0])

    while user_name not in list_borrower or user_name not in list_users: # Checking negative cases where user name inputted has not rent a book or not registered.
        if user_name not in list_users: 
            print('')
            print('User is not registered')
            print('')

        else:
            print('')
            print('Sorry, this user has not rent a book yet.')
            print('')

        print('')
        print('[ 1 ] Enter another user name')
        print('[   ] Press any key to return to book menu')
        print('')
        user_input = input('Insert your option: ')

        if user_input == '1':
            print('')
            user_name = input('Borrower\'s user name: ').title()
        else:
            return ('')

    db_con.mycursor.execute( # Fetching user data from rents database that matched with the user name inputted.
        """
        SELECT *
        FROM rents
        WHERE user_name = %s
        """,(user_name,)
    )

    user_rent_data = list(db_con.mycursor.fetchone())
    book_id = user_rent_data[2]

    db_con.mycursor.execute( # Updating (adding) book stock.
        """
        UPDATE books
        SET book_stock = book_stock+1
        WHERE book_id = (%s)
        """,(book_id,)
    )

    db_con.mycursor.execute( # Updating (deleting user) rents database
        """
        DELETE FROM rents
        WHERE user_name = (%s)
        """,(user_name,)
    )

    db_con.mycursor.execute( # Showing book data that has been updated
        """
        SELECT *
        FROM books
        WHERE book_id = (%s)
        """,(book_id,)
    )

    print('Book successfuly returned, book stock updated.')
    print('')
    
    book_data = db_con.pd.DataFrame(db_con.mycursor.fetchall())
    book_data.columns = db_con.mycursor.column_names
    print(book_data)

    db_con.db.commit()

        

