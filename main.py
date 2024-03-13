import sqlite3
import random

# Connecting & Creating new sqlite3 database
connection = sqlite3.connect("book.db")
cursor = connection.cursor()

# Creating Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS book (
    name TEXT,
    book_pages INTEGER,
    cover_type TEXT,
    category TEXT
)
""")

# Generating 10 randomly generated book entries
for _ in range(10):
    name = 'Book' + str(random.randint(1, 100))
    book_pages = random.randint(1, 500)
    cover_type = random.choice(["Hardcover", "Paperback", "E-book"])
    category = random.choice(["Fiction", "Non-Fiction", "Science Fiction", "Mystery", "Biography"])

    cursor.execute("INSERT INTO book (name, book_pages, cover_type, category) VALUES (?, ?, ?, ?)", (name, book_pages, cover_type, category))
    connection.commit()

# guessing number of average book pages
avg_book_pages = "SELECT AVG(book_pages) FROM book"
cursor.execute(avg_book_pages)

# Fetching the result
avg_book_pages_result = cursor.fetchone()[0]

# guessing How many pages does the largest book
big_book_by_pages = "SELECT MAX(book_pages) FROM book"
cursor.execute(big_book_by_pages)

# Fetching the result
big_book_pages_result = cursor.fetchone()[0]

# Printing the average number of pages
print("Average number of pages in the books:", avg_book_pages_result)

# Printing How many pages does the largest book print here
print("Big Book Name, by Pages is: ", big_book_pages_result)

# Closing Cursor
cursor.close()
# Closing database
connection.close()
