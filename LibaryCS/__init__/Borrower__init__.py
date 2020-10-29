import sqlite3 as sq3


DATABASE_NAME = "library.db"

CREATE_BORROW_TABLE = """
CREATE TABLE Borrower(
BorrowerID INTEGER PRIMARY KEY AUTOINCREMENT,
firstName VARCHAR(255)  NOT NULL, 
lastName VARCHAR(255)   NOT NULL,
address VARCHAR(255)    NOT NULL,
staffYN BOOL    NOT NULL
)
"""

INSERT_INTO_BORROW_TABLE = """INSERT INTO Borrower  (firstName, lastName, address, staffYN )
VALUES (?, ?, ?, ?)"""

with sq3.connect(DATABASE_NAME) as db:
    cursor = db.cursor()
    cursor.execute(CREATE_BORROW_TABLE)
    cursor.execute(INSERT_INTO_BORROW_TABLE, [
                   "Harry", "Turner","73 kold str",0])

