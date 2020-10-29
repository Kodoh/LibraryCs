import sqlite3 as sq3


DATABASE_NAME = "library.db"

CREATE_BOOK_TABLE = """
CREATE TABLE Book(
BookID INTEGER PRIMARY KEY AUTOINCREMENT,
ISBN VARCHAR(255)   NOT NULL,
BookName VARCHAR(255)  NOT NULL, 
BookAuthor VARCHAR(255)   NOT NULL,
BookTaken BOOL  NOT NULL,
BookDamaged BOOL    NOT NULL,
BookLost BOOL   NOT NULL,
BookBinned BOOL NOT NULL
)
"""

INSERT_INTO_BOOK_TABLE = """INSERT INTO Book  (ISBN, BookName, BookAuthor , BookTaken, BookDamaged, BookLost, BookBinned)
VALUES (?, ?, ?, ?, ?, ?, ?)"""


with sq3.connect(DATABASE_NAME) as db:
    cursor = db.cursor()
    cursor.execute(CREATE_BOOK_TABLE)
    cursor.execute(INSERT_INTO_BOOK_TABLE, [
                   "978-1-85798-334-0", "The Eternal Champion", "Michael Moorcock", 0, 1, 0, 0])
    cursor.execute(INSERT_INTO_BOOK_TABLE, [
                   "978-3-16-148410-0", "The Picture Of Dorian Gray", "Oscar Wilde", 1, 0, 0, 0])
    cursor.execute(INSERT_INTO_BOOK_TABLE, [
                   "978-6-22-177480-0", "Life Long", "Jim Martin", 1,0,0,0])
    cursor.execute(INSERT_INTO_BOOK_TABLE, [
                   "978-0-5675-6480-0", "The Maze Runner", "James Dashner", 0,0,1,0])
    cursor.execute(INSERT_INTO_BOOK_TABLE, [
                   "978-3-383-38348-0", "The Witcher", "Andrzej Sapkowski", 0,1,0,1])
    db.commit()
    pass
