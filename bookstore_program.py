import sqlite3
# import pandas as pd

# Creating the SQL database

conn = sqlite3.connect('bookstore')
c = conn.cursor()

# Creating the table

c.execute('''CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY,title TEXT,author TEXT, qty INTEGER)''')
conn.commit()

# Creating a function to enter new book information, and then also integrating it into the database

def enter_book():
    id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    c.execute("INSERT INTO bookstore(id, title, author, qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
    print("Your new book information has been added\n")

#  Creating a function to update book information, and then also integrating it into the database

def update_book():
    id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    c.execute("UPDATE bookstore SET id=?, title=?, author=? WHERE id=?", (id, title, author, qty))
    conn.commit()
    if c.rowcount == 0:
        print("Book not found")
    else:
        print("Book updated successfully!\n")

# Creating a function to delete a books information from the database

def delete_book():
    id = input("Enter book id: ")
    c.execute("DELETE FROM bookstore WHERE id=?", (id,))
    conn.commit()
    if c.rowcount == 0:
        print("Book not found!")
    else:
        print("Book deleted successfully!\n")

# Creating a function to search for books in the database and printing out their information

def search_book():
    id = input("Enter book id: ")
    c.execute("SELECT * FROM bookstore WHERE id=?", (id,))
    book = c.fetchone()
    if book is None:
        print("Book not found!\n")
    else:
        print("ID:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Quantity", book[3])
        print()

# Creating a while loop to keep sending the user back to the menu until they exit

while True:
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search book")
    print("5. Exit")

    # Creating a conditional for the user to select from a menu which is linked to the function calls of the functions above

    choice = int(input("Enter your choice: "))
    if choice == 1:
        enter_book()
    elif choice == 2:
        update_book()
    elif choice == 3:
        delete_book()
    elif choice == 4:
        search_book()
    elif choice == 5:
        break
    else:
        print("Invalid choice!\n")

# Giving variables to the table data

id1 = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30

id2 = 3002
title2 = 'Harry Potter and the Philosophers Stone'
author2 = 'J.K Rowling'
qty2 = 48

id3 = 3003
title3 = 'The Lion, the Witch and the Wardrobe'
author3 = 'CS Lewis'
qty3 = 25

id4 = 3004
title4 = 'The Lord of the Rings'
author4 = 'J.R.R Tolkien'
qty4 = 37

id5 = 3005
title5 = 'Alice in Wonderland'
author5 = 'Lewis Carroll'
qty5= 12

conn.commit()

# Inserting the data into the table

c.execute('''INSERT INTO bookstore (ID, TITLE, AUTHOR, QTY)
          VALUES(?,?,?,?)''',(id1, title1, author1, qty1))
c.execute('''INSERT INTO bookstore (ID, TITLE, AUTHOR, QTY)
          VALUES(?,?,?,?)''',(id2, title2, author2, qty2))
c.execute('''INSERT INTO bookstore (ID, TITLE, AUTHOR, QTY)
          VALUES(?,?,?,?)''',(id3, title3, author3, qty3))
c.execute('''INSERT INTO bookstore (ID, TITLE, AUTHOR, QTY)
          VALUES(?,?,?,?)''',(id4, title4, author4, qty4))
c.execute('''INSERT INTO bookstore (ID, TITLE, AUTHOR, QTY)
          VALUES(?,?,?,?)''',(id5, title5, author5, qty5))

# df = pd.DataFrame(c.fetchall(), columns=['ID','TITLE','AUTHOR','QTY'])
# print (df)

conn.commit()
conn.close()