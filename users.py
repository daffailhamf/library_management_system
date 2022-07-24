import db_con
    
def register():
    """
    Registering new user to database.

    User input:
        user_name (str): User name
        user_occupation (str): User occupation
        user_address (str): User address
    """
    print('')
    print('-----------------------------------------------')
    print('              Register new user'                )
    print('-----------------------------------------------')
    print('')
    try:    
        user_name = input(f'User name: ').title()
        user_occupation = input(f'Occupation: ').title()
        user_address = input(f'Address: ').title()
        print('')

        db_con.mycursor.execute( # Inserting new user's data to database
            """
            INSERT INTO users (user_name, user_occupation, user_address) 
            VALUES (%s,%s,%s);
            """, (user_name, 
                user_occupation, 
                user_address)
        )
        print('User registration success!')
        print('')
        input('Press any key to return to main menu: ')
        db_con.db.commit()
        return ('')

    except: # User name duplication defense
        print('Registration failed. User name already exist')
        print('')
        input('Press any key to return to main menu: ')
        return ('')

def fetch_database():
    """
    Showing all user data in the database. As the database grow, the amount of the data shown will be adjusted.
    """
    print('')
    print('-----------------------------------------------')
    print('                 User database'                 )
    print('-----------------------------------------------')
    print('')
    db_con.mycursor.execute(
    """
    SELECT * FROM users;
    """
    )
    try:
        user_database = db_con.pd.DataFrame(db_con.mycursor.fetchall())
        user_database.columns = db_con.mycursor.column_names
        print(user_database)
    except:
        print('No user in the database')
    
    print('')
    input('Press any key to return to main menu: ')
    return ('')