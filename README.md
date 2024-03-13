# Book Database Management
This Python script manages a SQLite3 database for storing information about books. It creates a database file named book.db, creates a table named book within it, and populates the table with 10 randomly generated book entries. Additionally, it performs some basic queries on the database to retrieve information such as the average number of pages in the books and the details of the book with the maximum number of pages.

# Prerequisites
- Python 3.x
- SQLite3 library (sqlite3)

# Setup Instructions
- Make sure Python is installed on your system.
- Ensure you have the SQLite3 library installed. If not, you can install it using pip:
'''Copy code:
pip install sqlite3'''
- Copy the provided code into a Python file (e.g., book_database.py).
# Usage
Run the script using Python:
Copy code
'''python book_database.py'''

# Description
- The script connects to a SQLite3 database (book.db) and creates a table named book if it doesn't already exist.
It generates 10 random book entries with attributes such as name, number of pages, cover type, and category, and inserts them into the database.
After populating the database, it performs two queries:
It calculates the average number of pages across all the books stored in the database.
It retrieves details about the book with the maximum number of pages.
The results of these queries are printed to the console.

# Database Schema
The book table schema consists of the following columns:

name: Textual name of the book.
book_pages: Integer representing the number of pages in the book.
cover_type: Text indicating the cover type of the book (e.g., Hardcover, Paperback, E-book).
category: Text specifying the category of the book (e.g., Fiction, Non-Fiction, Science Fiction, Mystery, Biography).

# Notes
This script generates random book entries for demonstration purposes. In a real-world scenario, you would replace the random data generation with actual data inputs.
Ensure proper error handling and input validation are implemented before deploying this script in a production environment.
For any further modifications or enhancements, refer to the comments within the script for guidance.
