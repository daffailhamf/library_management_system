# Library Management System

This is a mini-project for my Python class assignment. The project aims to build a library management system in Python that is connected to the MySql database.  
  
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

## Features usage guidelines  

**-- Register a new user --**  
This feature will add a new user to the user's database. The user name must be a unique value.  
The user's attributes in the user's database are:  
1. User ID (Primary key) auto increment
2. User name  
3. User occupation
4. User address 
  
User flow:  
1. New users come to the offline library
2. New users come to the admin desk in front of the entrance door
3. Admin will input the required data into the program

How to register new users inside the system:  
1. Run the program (main.py)
2. Choose option 1 by typing 1 in the terminal
3. Input all the required information
4. If the user name is not unique, the system will return a failed message.
5. If successful, the system will return a success message
6. Process completed
  
**-- Show user database --**  
This feature will show all user data inside the database.  

User flow:  
1. Admin wants to display all user data in the database
2. Admin will run the feature in the system

How to show the user database inside the system:  
1. Run the program (main.py)
2. Choose option 2 by typing 2 in the terminal
3. Process completed  

**-- Register new book --**  
This feature will add a new book to the book's database. Admin also has to input the stock of the book that is being registered. 

Books's attributes in the book's database are:  
1. Book ID (Primary key) auto increment
2. Book title  
3. Book Author
4. Book published year
5. Book stock 
  
User flow:  
1. Admin will input the required data in the program

How to register new users inside the system:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in the terminal
3. Choose option 1 by typing 1 in terminal
3. Input all the required information
5. The system will return a success message
6. Process completed  

**-- Show book database --**  
This feature will show all book data inside the database.  

User flow:  
1. Admin wants to display all book data in the database
2. Admin will run the feature in the system

How to show the book database inside the system:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in the terminal
3. Choose option 2 by typing 2 in the terminal  
4. Process completed  
  

**-- Search book in the database --**  
This feature will show all book data inside the database.  

User flow:  
1. Admin wants to display specific book data in the database
2. Admin will run the feature in the system

How to display specific book data in the database inside the system:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in the terminal
3. Choose option 3 by typing 3 in the terminal  
4. Input all requirements (why I require book title, author and published year in the input is because in real life, one title can be used in many books. So inputting the title alone is not enough to get specific results)
5. If the book is not found, the system will return a failed message
6. If the book is found, the system will return the book's data  

**-- Rent a book --**  
This feature will data all users that want to rent a book. One user can only rent one book at a time. If the user wants to rent another book, the user will have to return the previous book that is being rented. The user is given 7 days at most to return a book that is being rented. The rent date and return date are automatically generated. 

User flow:  
1. The user comes to the admin desk bringing a book that wants to be rented. Or users can ask at the admin desk, for the book that want to be rented.
2. If the user is asking the admin, the admin will ask for the specific attribute of the book to the user, such as the book title, book author, and the published year.
3. If the user brings the book to the admin desk, then the admin will search for the attributes inside the book or on the internet
4. Admin will run the feature in the system

How to rent a book:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in the terminal
3. Choose option 4 by typing 4 in the terminal  
4. Input the user name to check whether the user name inputted is registered or not, and to check whether the user name inputted has not returned a book.
5. If the user name is not found, system will return a failed message
6. If the user has not returned a book, the system will return a failed message
7. Checking book availability by inputting book's attributes such as book's title, book's author, and book's published year
8. If the book is not yet registered, the system will return a failed message
9. If the book is out of stock, the system will return a failed message
10. If the book is found, the system will add the user to the rent database, decreasing book stock in the book database
11. The system will return a success message  
  
**-- Return a book --**  
This feature will update book stock in the book's database and delete users from the rent database. 

User flow:  
1. The user comes to the admin desk bringing a book that wants to be returned.
2. Admin will ask the user's user name.
3. Admin will run the feature in the system

How to return a book:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in the terminal
3. Choose option 5 by typing 5 in the terminal  
4. Input the user name to check whether the user name inputted is registered or not, and to check whether the user name inputted is indeed renting a book or not.
5. If the user name is not found, system will return a failed message
6. If the user has not rented a book, the system will return a failed message
7. If the user is found in the rent's database, the system will return a success message  
  
**-- Show rent database --**  
This feature will show all user's data inside the rent database.  

User flow:  
1. Admin wants to display all user's data in the rent database
2. Admin will run the feature in the system

How to show the rent database inside the system:  
1. Run the program (main.py)
2. Choose option 3 by typing 3 in the terminal
3. Choose option 6 by typing 6 in the terminal  
4. Process completed  
