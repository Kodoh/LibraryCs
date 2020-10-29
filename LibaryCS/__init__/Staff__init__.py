import sqlite3 as sq3


DATABASE_NAME = "library.db"

CREATE_STAFF_TABLE = """
CREATE TABLE LibStaff(
LibID INTEGER PRIMARY KEY AUTOINCREMENT,
LastName varchar(255)   NOT NULL,
FirstName varchar(255)  NOT NULL, 
Username varchar(255)   NOT NULL,
Password varchar(255)   NOT NULL
)
"""

INSERT_INTO_STAFF_TABLE = """INSERT INTO LibStaff  (LastName, FirstName, Username , Password )
VALUES (?, ?, ?, ?)"""

with sq3.connect(DATABASE_NAME) as db:
    cursor = db.cursor()
    cursor.execute(CREATE_STAFF_TABLE)
    cursor.execute(INSERT_INTO_STAFF_TABLE, ["Jake", "Anderson", "JAnderson", "Jand"])
    cursor.execute(INSERT_INTO_STAFF_TABLE, ["Noah", "Smith", "NSmith", "Nsmi"])
    cursor.execute(INSERT_INTO_STAFF_TABLE, ["Kate", "Weston", "KWeston", "Kwes"])
    cursor.execute(INSERT_INTO_STAFF_TABLE, ["Chloe", "Lee", "CLee", "Clee"])
    cursor.execute(INSERT_INTO_STAFF_TABLE, ["Ryan", "Rivia", "RRivia", "Rriv"])
    db.commit()
    pass




