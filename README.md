# Library Management System

This is a mini project for my python class assignment. The project aims to built a library management system in python that is connected to MySql database.  
  
Assumption:  
- This program will be used in an offline library environment
- This program will be used by the library Admin
## Features
1. Register new user
2. Show user database
3. Register new book
4. Show book database
5. Search book in the database
6. Rent a book
7. Return a book
8. Show rent database  
## Features usage guidlines  

**-- Register new user --**  
This feature will add a new user to the user's database. User name must be unique value.  
User's attributes in user's database are:  
1. User id (Primary key) auto increment
2. User name  
3. User occupation
4. User address 
  
User flow:  
1. New user come to the offline library
2. New user come to the admin desk in front of the entrance door
3. Admin will input the required data in the program

How to register new user inside the system:  
1. Run the program (main.py)
2. Choose option 1 by typing 1 in terminal
3. Input all the required information
4. If user name is not unique, system will return failed message.
5. If succes, system will return success message
6. Process completed
  
**-- Show user database --**  
This feature will show all user data inside the database.  

User flow:  
1. Admin wants to display all user data in the database
2. Admin will run the feature in the system

How to show user database inside the system:  
1. Run the program (main.py)
2. Choose option 2 by typing 2 in terminal
3. Process completed  

**-- Register new book --**  
This feature will add new a book to the book's database. Admin also has to input the stock of the book that is being registered. 

Books's attributes in book's database are:  
1. Book id (Primary key) auto increment
2. Book title  
3. Book author
4. Book published year
5. Book stock 
  
User flow:  
1. Admin will input the required data in the program

How to register new user inside the system:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in terminal
3. Choose option 1 by typing 1 in terminal
3. Input all the required information
5. System will return success message
6. Process completed  

**-- Show book database --**  
This feature will show all book data inside the database.  

User flow:  
1. Admin wants to display all book data in the database
2. Admin will run the feature in the system

How to show book database inside the system:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in terminal
3. Choose option 2 by typing 2 in terminal  
4. Process completed  
  

**-- Search book in the database --**  
This feature will show all book data inside the database.  

User flow:  
1. Admin wants to display specific book data in the database
2. Admin will run the feature in the system

How to display specific book data in database inside the system:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in terminal
3. Choose option 3 by typing 3 in terminal  
4. Input all requirements (why i require book title, author and published year in the input is because in real life, one title can be used in many books. So inputting title alone is not enought to get specific result)
5. If book is not found, system will return failed message
6. If book is found, system will return book's data  

**-- Rent a book --**  
This feature will data all user that want to rent a book. One user can only rent one book at a time. If user want to rent another book, user will have to return previous book that being rented. User is given 7 days at most to return a book that is being rented. Rent date and return date is automatically generated. 

User flow:  
1. User come to the admin desk bringing a book that want to be rented. Or user can ask in the admin desk, the book that want to be rented.
2. If user is asking the admin, admin will ask the specific attribute of the book to the user, such as the book title, book author, and the published year.
3. If the user is bring the book to the admin desk, than admin will search for the attributes inside the book or in the internet
4. Admin will run the feature in the system

How to rent a book:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in terminal
3. Choose option 4 by typing 4 in terminal  
4. Input user name to check whether the user name inputted is registered or not, and to check whether user name inputted has not returned a book.
5. If user name is not found, system will return failed message
6. If user has not returned a book, system will return failed message
7. Checking books availability by inputting book's attribute such as book's title, book's author, and book's published year
8. If the book is not yet registered, the system will return failed message
9. If the book is out of stock, system will return failed message
10. If the book is found, system will add user to the rent database, decreasing book stock in the book database
11. System will return success message  
  
**-- Return a book --**  
This feature will update book stock in the book's database and delete user from the rent's database. 

User flow:  
1. User come to the admin desk bringing a book that want to be returned.
2. Admin will ask the user's user name.
3. Admin will run the feature in the system

How to return a book:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in terminal
3. Choose option 5 by typing 5 in terminal  
4. Input user name to check whether the user name inputted is registered or not, and to check whether user name inputted is indeed renting a book or not.
5. If user name is not found, system will return failed message
6. If user has not rent a book, system will return failed message
7. If the user is found in the rent's database, system will return success message  
  
**-- Show rent database --**  
This feature will show all users data inside the rent database.  

User flow:  
1. Admin wants to display all users data in the rent database
2. Admin will run the feature in the system

How to show rent database inside the system:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in terminal
3. Choose option 6 by typing 6 in terminal  
4. Process completed  
## Technology
1. Python version: 3.9
2.   

  
## Weakness & Limitations
1. Code readability & efficiency
2. File, database, and programm structure 
