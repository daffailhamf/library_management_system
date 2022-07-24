import mysql.connector as mysql
import pandas as pd

db = mysql.connect( # Making connection to mysql
    host = 'localhost', 
    user = 'root', 
    passwd = 'serversql', 
    database = 'library_management_system'
)

mycursor = db.cursor(buffered=True)

mycursor.execute( # Creating users table
"""
CREATE TABLE IF NOT EXISTS users(
    user_id INT AUTO_INCREMENT,
    user_name VARCHAR (50) UNIQUE NOT NULL,
    user_occupation VARCHAR (50) NOT NULL,
    user_address VARCHAR (50) NOT NULL,
    PRIMARY KEY (user_id)
);
"""
)

mycursor.execute( # Creating books table
    """
    CREATE TABLE IF NOT EXISTS books(
        book_id INT AUTO_INCREMENT,
        book_title VARCHAR (50) NOT NULL,
        book_author VARCHAR (50),
        book_published_year VARCHAR (4),
        book_stock INT,
        PRIMARY KEY (book_id)
    )
    """
)

mycursor.execute( # Creating rents table
    """
    CREATE TABLE IF NOT EXISTS rents(
        user_id INT,
        user_name VARCHAR (50) NOT NULL,
        book_id INT NOT NULL,
        book_title VARCHAR (50) NOT NULL,
        rent_date DATE NOT NULL,
        return_date DATE NOT NULL,
        PRIMARY KEY (user_id),
        FOREIGN KEY (user_id) REFERENCES users (user_id),
        FOREIGN KEY (book_id) REFERENCES books (book_id)
    )
    """
)