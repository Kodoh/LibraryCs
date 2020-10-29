import sys
import sqlite3
sys.path.append(sys.path[0] + "/../classes")
import classes.BookClass as BookClass
import classes.LibStaffClass as LibStaffClass

DATABASE_NAME = "library.db"

def insertBook(book):
    INSERT_INTO_BOOK_TABLE = """INSERT INTO Book  (ISBN, BookName, BookAuthor , BookTaken , BookDamaged, BookLost, BookBinned)
    VALUES (?, ?, ?, ?, ?, ?, ?)"""
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(INSERT_INTO_BOOK_TABLE, [book.getISBN(),book.getTitle(),book.getAuthor(),book.getIsTaken(),book.getIsDamaged(),book.getIsLost(),book.getIsBinned()])
        db.commit()
        pass
    return True


def insertStudent(borrower):
    INSERT_INTO_BORROW_TABLE = """INSERT INTO Borrower  (firstName, lastName, address, staffYN )
    VALUES (?, ?, ?, ?)"""
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(INSERT_INTO_BORROW_TABLE, [borrower.getFirstName(),borrower.getSurname(),borrower.getAddress(),borrower.getStaffYN()])
        db.commit()
        pass

def insertBorrowerStaff(borrower):
    INSERT_INTO_BORROW_TABLE = """INSERT INTO Borrower  (firstName, lastName, address, staffYN )
    VALUES (?, ?, ?, ?)"""
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(INSERT_INTO_BORROW_TABLE, [borrower.getFirstName(),borrower.getSurname(),borrower.getAddress(),True])
        db.commit()
        pass

def BookAuthorSearch(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select * from Book where BookAuthor = {book.getAuthor()}")
        authorId = list(cursor.fetchone())
        return authorId

def BookTitleSearch(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select * from Book where BookName = {book.getTitle()}")
        titleId = list(cursor.fetchone())
        return titleId

def DamagedBookSearch(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BookName from Book where BookDamaged = 1")
        BookDam = cursor.fetchall()
        return BookDam 

def SelectDamagedCheck(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BookDamaged from Book where BookID = {book.getID()}")
        ReturnDamCheck = cursor.fetchone()
        return ReturnDamCheck

def SelectBinnedCheck(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BookBinned from Book where BookID = {book.getID()}")
        ReturnBinCheck = cursor.fetchone()
        return ReturnBinCheck


def SelectLostCheck(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BookLost from Book where BookID = {book.getID()}")
        ReturnLostCheck = cursor.fetchone()
        return ReturnLostCheck


def LostBookSearch(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BookName from Book where BookLost = 1")
        BookLost = cursor.fetchall()
        return BookLost

def BinnedBookSearch(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BookName from Book where BookBinned")
        BookBin = cursor.fetchall()
        return BookBin

def AddDamagedBook(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BookDamaged from Book where BookID = {book.getID()}")
        bookDam = cursor.fetchall()[0][0]
        if bookDam == False:
            sql = f"update Book set BookDamaged=1 where BookID = {book.getID()}"
            cursor.execute(sql)
            db.commit()
            return bookDam
        else:
            return bookDam

def AddLostBook(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor.execute(f"select BookLost from Book where BookID = {book.getID()}")
        bookLost = cursor.fetchall()[0][0]
        if bookLost == False:
            sql = f"update Book set BookLost=1 where BookID = {book.getID()}"
            cursor.execute(sql)
            db.commit()
            return bookLost
        else:
            return bookLost

def AddBinnedBook(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor.execute(f"select BookBinned from Book where BookID = {book.getID()}")
        bookBin = cursor.fetchall()[0][0]
        if bookBin == False:
            sql = f"update Book set BookBinned=1 where BookID = {book.getID()}"
            cursor.execute(sql)
            db.commit()
            return bookBin
        else:
            return bookBin

def SelectAllIDs(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BookID from Book")
        ID = list(cursor.fetchall())
        return ID

def SelectAllFnames(borrower):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select firstName from Borrower")
        Fname = list(cursor.fetchall())
        return Fname

def SelectAllBorrowerIDs(borrower):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BorrowerID from Borrower")
        BorrowerId = list(cursor.fetchall())
        return BorrowerId   

def SelectAllLnames(borrower):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select lastName from Borrower")
        Lname = list(cursor.fetchall())
        return Lname

def SelectAllAuthor(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BookAuthor from Book")
        Author = list(cursor.fetchall())
        return Author

def SelectAllTitles(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BookName from Book")
        BookNames = list(cursor.fetchall())
        return BookNames

def SelectLastID(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BookID from Book")
        lastID = list(cursor.fetchall())[-1]
        return lastID

def SelectBooksTaken(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BookName from Book where BookTaken > 0")
        takenName = list(cursor.fetchall())
        return takenName
    

def SelectBookID(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        # need to add error for if not valid ID
        cursor.execute(f"select BookTaken from Book where BookID = {book.getID()}")
        bookTake = cursor.fetchall()[0][0]
        return bookTake

def SelectBorrowerLNameToday(borrowed):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BorrowerLName from Borrowed where DueDate = {borrowed.getBorrowedDate()}")
        bookTakeTodayLName = list(cursor.fetchall())
    return bookTakeTodayLName

def SelectBorrowerFNameToday(borrowed):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BorrowerFName from Borrowed where DueDate = {borrowed.getBorrowedDate()}")
        bookTakeTodayFName = list(cursor.fetchall())
        return bookTakeTodayFName

def SelectBorrowedIDToday(borrowed):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BorrowedID from Borrowed where DueDate = {borrowed.getBorrowedDate()}")
        BorrowedIDToday = list(cursor.fetchall())
        return BorrowedIDToday

def SelectOverDueID(borrowed):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BookID from Borrowed where DueDate > {borrowed.getBorrowedDate()}")
        bookTake = list(cursor.fetchall())
        return bookTake

def SelectOverDueBorrowedID(borrowed):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BorrowedID from Borrowed where DueDate = {borrowed.getBorrowedDate()}")
        BorrowedID = list(cursor.fetchall())
        return BorrowedID


def SelectBookIDToday(borrowed):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BookID from Borrowed where DueDate = {borrowed.getBorrowedDate()}")
        bookTakeTodayID = list(cursor.fetchall())
        return bookTakeTodayID

def SelectOverDueFName(borrowed):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BorrowerFName from Borrowed where DueDate > {borrowed.getBorrowedDate()}")
        bookTakeFname = list(cursor.fetchall())
        return bookTakeFname

def SelectOverDueLName(borrowed):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BorrowerLName from borrowed where DueDate > {borrowed.getBorrowedDate()}")
        bookTakeLName = list(cursor.fetchall())
        return bookTakeLName

def DeleteID(borrowed):
        with sqlite3.connect(DATABASE_NAME) as db:
            cursor = db.cursor()
            sql = f"delete from Borrowed where BookID = {borrowed.getBookID()}"
            cursor.execute(sql)

def SelectBookTakenID(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BookTaken from Book where BookID = {book.getID()}")
        bookTake = cursor.fetchall()[0][0]
        return bookTake  

def UpdateBookTaken(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        sql = f"update Book set BookTaken=0 where BookID = {book.getID()}"
        cursor.execute(sql)
        db.commit()

def SelectBookTakenIDFromBook(book): 
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select BookTaken from Book where BookID = {book.getID()}")
        bookTake = cursor.fetchall()[0][0]
        return bookTake

def SelectStaffYN(borrower):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select staffYN from Borrower where BorrowerID = {borrower.getBorrowerID()}")
        staffCheck = cursor.fetchall()[0][0]
        return staffCheck

def InsertBorrowedTableStudent(borrowed):
    INSERT_INTO_BORROWED_TABLE = """INSERT INTO Borrowed  (BorrowerFName, BorrowerLName, BookID, BorrowDate, DueDate)
    VALUES (?, ?, ?,?,?)"""
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(INSERT_INTO_BORROWED_TABLE, [f"{borrowed.getBorrowedFName()}",f"{borrowed.getBorrowedLName()}",f"{borrowed.getBookID()}",f"{borrowed.getBorrowedDate()}",f"{borrowed.getDueDate()}"])
        db.commit()
        pass

def UpdateBookTakenStatus(book):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        sql = f"update Book set BookTaken=1 where BookID = {book.getID()}"
        cursor.execute(sql)
        db.commit()

def InsertBorrowedTableStaff(borrowed):
    INSERT_INTO_BORROWED_TABLE = """INSERT INTO Borrowed  (BorrowerFName, BorrowerLName, BookID, BorrowDate, DueDate)
    VALUES (?, ?, ?,?,?)"""
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(INSERT_INTO_BORROWED_TABLE, [f"{borrowed.getBorrowedFName()}",f"{borrowed.getBorrowedLName()}",f"{borrowed.getBookID()}",f"{borrowed.getBorrowedDate()}",f"{borrowed.getDueDate()}"])
        db.commit()
        pass

def SelectUsername(LibS):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select Username from LibStaff where LibID = {LibS.getLibID()}")
        username = cursor.fetchone()[0]
        return username

def SelectPassword(LibS):
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute(f"select Password from LibStaff where LibID = {LibS.getLibID()}")
        password = cursor.fetchone()[0]
        return password