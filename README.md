# Library Management System

This repository contains a Python-based Library Management System connected to a MySQL database. It was developed as part of a Python class assignment.

## Assumptions

- The program is designed for an offline library environment.
- It is intended for use by library administrators.

## Features

1. **Register New User**
2. **Show User Database**
3. **Register New Book**
4. **Show Book Database**
5. **Search Book in the Database**
6. **Rent a Book**
7. **Return a Book**
8. **Show Rent Database**

## Feature Usage Guidelines

### Register a New User

- Adds a new user to the database with a unique username.
- User attributes in the database:
  - User ID (Primary key, auto-increment)
  - User name
  - User occupation
  - User address

**User Flow:**
1. New users visit the offline library.
2. Users approach the admin desk.
3. Admin inputs required user data into the program.

### Show User Database

- Displays all user data from the database.

**Admin Flow:**
1. Admin wants to view all user data.
2. Admin accesses this feature in the system.

### Register New Book

- Adds a new book to the database, including specifying the stock quantity.

**Book Attributes in the Database:**
  - Book ID (Primary key, auto-increment)
  - Book title
  - Book author
  - Book published year
  - Book stock

**Admin Flow:**
1. Admin inputs required book data into the program.

### Show Book Database

- Displays all book data from the database.

**Admin Flow:**
1. Admin wants to view all book data.
2. Admin accesses this feature in the system.

### Search Book in the Database

- Searches for specific book data in the database based on title, author, and published year.

**Admin Flow:**
1. Admin wants to find specific book data.
2. Admin accesses this feature in the system and provides the necessary attributes for search.

### Rent a Book

- Records users' requests to rent a book.
- Each user can rent only one book at a time with a maximum return period of 7 days.

**User Flow:**
1. Users come to the admin desk to rent a book.
2. Admin searches for the book or attributes.
3. Admin initiates the rental process in the system.

### Return a Book

- Updates the book stock in the database and removes users from the rent database upon book return.

**User Flow:**
1. Users return books to the admin desk.
2. Admin checks the user's username.
3. Admin completes the return process in the system.

### Show Rent Database

- Displays all user data in the rent database.

**Admin Flow:**
1. Admin wants to view user rental data.
2. Admin accesses this feature in the system.

