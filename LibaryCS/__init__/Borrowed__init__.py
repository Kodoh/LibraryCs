import sqlite3 as sq3


DATABASE_NAME = "library.db"

CREATE_BORROWED_TABLE = """
CREATE TABLE Borrowed(
BorrowedID INTEGER PRIMARY KEY AUTOINCREMENT,
BorrowerFName VARCHAR(255)  NOT NULL, 
BorrowerLName VARCHAR(255)   NOT NULL,
BookID INT    NOT NULL,
BorrowDate VARCHAR(255)  NOT NULL,
DueDate VARCHAR(255) NOT NULL
)
"""


INSERT_INTO_BORROWED_TABLE = """INSERT INTO Borrowed    (BorrowerFName, BorrowerLName, BookID, BorrowDate, DueDate)
VALUES (?,?,?,?,?)"""

with sq3.connect(DATABASE_NAME) as db:
    cursor = db.cursor()
    cursor.execute(CREATE_BORROWED_TABLE)

