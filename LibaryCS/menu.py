import sys
sys.path.append(sys.path[0] + "/Actions")
sys.path.append(sys.path[0] + "/Actions/classes")
import sqlite3
import datetime
from dateutil.relativedelta import *
import SQLfunctions
import classes.BookClass as BookClass
import classes.BorrowerClass as BorrowerClass
import classes.ItemBorrowedClass as ItemBorrowedClass

BOOKCAPSTUDENT = 2
BOOKCAPSTAFF = 4
DATABASE_NAME = "library.db"


def LibMenu():
    print("""\nMenu options:

    1. New Book                 
    2. Lost/damaged/binned book
    3. Add new student
    4. Add new staff (teachers)
    5. Check-out a book
    6. Check-in a book
    7. Check the status of a book
    8. Due books
    9. Find a book (via book title / author)
    10. Reports
    11. To exit menu""")
    try:
        option = int(input("\nPlease select an option: "))
    except ValueError:
        raise ValueError(LibMenu())
    if option == 7:
        status()
    elif option == 11:
        sys.exit()
    elif option == 6:
        CheckIn()
    elif option == 5:
        CheckOut()
    elif option == 9:
        Search()
    elif option == 10:
        reports()
    elif option == 1:
        AddBook()
    elif option == 3:
        AddStudent()
    elif option == 4:
        AddTeacher()
    elif option == 8:
        DueBook()
    elif option == 2:
        Issue()
    else:
        print("invalid number try again")
        LibMenu()


def status():
    try:
        bookid = int(input("Enter the ID of the book you want to know about: "))
    except ValueError:
        raise ValueError(LibMenu())
    book = BookClass.Book(bookid, "", "", False,
                    "", False, False)
    SelectAllIDs = SQLfunctions.SelectAllIDs(book)
    NewIdList = [ele[0] for ele in SelectAllIDs]
    if bookid not in NewIdList:
        print("\nID does not exist")
        LibMenu()
    else:
        SelectBookID = SQLfunctions.SelectBookID(book)
        if SelectBookID == True:
            print("\nBook is currently taken")
            LibMenu()
        else:
            print("\nBook is not currently taken")
            LibMenu()


def CheckIn():
    try:
        bookid = int(input("Enter the ID of the book you want to check in: "))
    except ValueError:
        raise ValueError(LibMenu())
    book = BookClass.Book(bookid, "", "", False,
                "", False, False)
    SelectAllIDs = SQLfunctions.SelectAllIDs(book)
    NewIdList = [ele[0] for ele in SelectAllIDs]
    if bookid not in NewIdList:
        print("\nID does not exist")
        LibMenu()
    else:
        SelectBookTakenID = SQLfunctions.SelectBookTakenID(book)
        if SelectBookTakenID == True:
            borrowed = ItemBorrowedClass.ItemBorrowed(0, "", "",
                            bookid, "", "")
            DeleteID = SQLfunctions.DeleteID(borrowed)
            UpdateBookTaken = SQLfunctions.UpdateBookTaken(book)
            print("\nBook has been checked in!")
            LibMenu()
        else:
            print("\nBook has already been checked in!")
            LibMenu()
# CheckIn()


def CheckOut():
    borrower = BorrowerClass.Borrower(0,"","","",False)
    global BorrowDate
    BorrowDate = datetime.date.today()
    try:
        bookid = int(input("Enter the ID of the book you want to check out: "))
    except ValueError:
        raise ValueError(LibMenu())
    book = BookClass.Book(bookid, "", "", False,
            "", False, False)
    SelectAllIDs = SQLfunctions.SelectAllIDs(book)
    NewIdList = [ele[0] for ele in SelectAllIDs]
    if bookid not in NewIdList:
        print("\nID does not exist")
        LibMenu()
    else:
        SelectBookTakenIDFromBook = SQLfunctions.SelectBookTakenIDFromBook(
            book)
        if SelectBookTakenIDFromBook == False:
            Fname = input("Please enter first name: ")  
            SelectAllFnames = SQLfunctions.SelectAllFnames(borrower)
            NewAllFnames = [ele[0] for ele in SelectAllFnames]
            if Fname not in NewAllFnames:
                print("\nInvalid name please make sure name is added to system")
                LibMenu()
            else:
                Lname = input("Please enter last name: ")
                SelectAllLnames = SQLfunctions.SelectAllLnames(borrower)
                NewAllLnames = [ele[0] for ele in SelectAllLnames]
                if Lname not in NewAllLnames:
                    print("\nInvalid name please make sure name is added to system")
                    LibMenu()
                else:
                    try:                    
                        ID = int(input("Please enter BorrowerID: "))
                    except ValueError:
                        raise ValueError(LibMenu())
                    SelectAllBorrowerIDs = SQLfunctions.SelectAllBorrowerIDs(borrower)
                    NewAllBorrowerIDs = [ele[0] for ele in SelectAllBorrowerIDs]
                    if ID not in NewAllBorrowerIDs:
                        print("\nInvalid ID please make sure ID is on system")
                        LibMenu()
                    else:
                        borrowed = ItemBorrowedClass.ItemBorrowed(0,Fname,Lname,bookid,BorrowDate,BorrowDate + relativedelta(days=+5))   ####
                        borrower = BorrowerClass.Borrower(ID,Fname,Lname,"",False)
                        SelectStaffYN = SQLfunctions.SelectStaffYN(borrower)
                        if SelectStaffYN == 0:
                            InsertBorrowedTableStudent = SQLfunctions.InsertBorrowedTableStudent(borrowed)
                            UpdateBookTakenStatus = SQLfunctions.UpdateBookTakenStatus(book)
                            print("\nBook has been checked out!")
                            LibMenu()
                        else:
                            borrowed = ItemBorrowedClass.ItemBorrowed(0,Fname,Lname,bookid,BorrowDate,BorrowDate + relativedelta(days=+10))
                            UpdateBookTakenStatus = SQLfunctions.UpdateBookTakenStatus(book)
                            InsertBorrowedTableStaff = SQLfunctions.InsertBorrowedTableStaff(borrowed)
                            print("\nBook has been checked out!")
                            #cursor = db.cursor()
                            LibMenu()
        else:
            print("\nBook has already been checked out!")
            LibMenu()

# CheckOut()


def Search():               # NEED TO SET UP ERROR IN CASE NAME / AUTHOR NOT FOUND
    book = BookClass.Book(0, "", "", "", False, False, False, False)
    try:
        authorTitle = int(input("Please enter 1 to search by author or enter 2 to search by title: "))
    except ValueError:
        raise ValueError(LibMenu())
    if authorTitle == 1:
        author = input("Please enter the name of the author you are looking for: ")
        SelectAllAuthor = SQLfunctions.SelectAllAuthor(book)
        NewAllAuthor = [ele[0] for ele in SelectAllAuthor]
        if author not in NewAllAuthor:
            print("\nAuthor not found!")
            LibMenu()
        else:
            authorq = f"'{author}'"
            book = BookClass.Book(0, "", "", authorq, False, False, False, False)
            authorRes = SQLfunctions.BookAuthorSearch(book)
            print(f"\nInfo about book from {author}: ")
            print(f"The ID of the book is {authorRes[0]}")
            #authorISBN = list(cursor.fetchone())[1]
            print(f"The ISBN of the book is {authorRes[1]}")
            print(f"The name of the book is {authorRes[2]}")
            if authorRes[4] == True:
                print("The book is currently taken out!")
                LibMenu()
            else:
                print("The book is not taken out")
                LibMenu()
    elif authorTitle == 2:
        title = input(
            "Please enter the name of the title you are looking for: ")
        SelectAllTitles = SQLfunctions.SelectAllTitles(book)
        NewAllTitles = [ele[0] for ele in SelectAllTitles]
        if title not in NewAllTitles:
            print("\nTitle not found!")
            LibMenu()
        else:
            titleq = f"'{title}'"
            book = BookClass.Book(0, "", titleq, "", False, False, False, False)
            TitleRes = SQLfunctions.BookTitleSearch(book)
            print(f"\nInfo about {title}: ")
            print(f"The ID of {title} is {TitleRes[0]}")
            #authorISBN = list(cursor.fetchone())[1]
            print(f"The ISBN of {title} is {TitleRes[1]}")
            print(f"The author of {title} is {TitleRes[3]}")
            if TitleRes[4] == True:
                print("The book is currently taken out!")
                LibMenu()
            else:
                print("The book is not taken out")
                LibMenu()
    else:
        print("invalid number please enter 1 or 2!")
        LibMenu()


def reports():
    print("\nReports:")
    book = BookClass.Book(0, "", "", False,
                    "", False, False)
    selectLastID = SQLfunctions.SelectLastID(book)
    print(f"There are {list(selectLastID)[0]} books")
    selectBooksTaken = SQLfunctions.SelectBooksTaken(book)
    for i in list(selectBooksTaken):
        print(f"{list(i)[0]} is currently borrowed")
    LibMenu()


def AddBook():  # needs to have error messages coded
    print("\nNew book:")
    ISBN = input("Please enter 13 digit ISBN (eg - 978-x-xx-xxxxxx-x): ")
    if len(ISBN) == 17:
        BookName = input("Please enter the name of the book: ")
        if BookName.strip():
            BookAuthor = input("Please enter the author of the book: ")
            if BookAuthor.strip():
                book = BookClass.Book(0, ISBN, BookName, BookAuthor)
                result = SQLfunctions.insertBook(book)
                if result == True:
                    print("Book has been added !")
                else:
                    print("Could not add book")
                LibMenu()
            else:
                print("\nPlease enter something!")
            LibMenu()
        else :
            print("\nPlease enter something!")
            LibMenu()
    else:
        print("Invalid ISBN")
        LibMenu()
# AddBook()


def AddStudent():
    print("\nNew student:")
    Fname = input("Please enter first name: ")
    if Fname.strip():
        Lname = input("Please enter surname: ")
        if Lname.strip():
            address = input("Please enter your address: ")
            if address.strip():
                # I think i can leave it as it defaults to false but not sure
                borrower = BorrowerClass.Borrower(0, Fname, Lname, address)
                BorrowerRes = SQLfunctions.insertStudent(borrower)
                print("Student has been added!")
                LibMenu()
            else:
                print("\nPlease enter something for input!")
                LibMenu()
        else:
            print("\nPlease enter something for name")
            LibMenu()
    else:
        print("\nPlease enter something for name")
        LibMenu()

# AddStudent()


def AddTeacher():
    print("\nNew teacher:")
    Fname = input("Please enter first name: ")
    if Fname.strip():
        Lname = input("Please enter surname: ")
        if Lname.strip():
            address = input("Please enter your address: ")
            if address.strip():
                borrower = BorrowerClass.Borrower(0, Fname, Lname, address, True)
                BorrowerRes = SQLfunctions.insertBorrowerStaff(borrower)
                print("Teacher has been added!")
                LibMenu()
            else:
                print("\nPlease enter something for name")
                LibMenu()
        else:
            print("\nPlease enter something for name")
            LibMenu()
    else:
        print("\nPlease enter something for name")
        LibMenu()


def DueBook():
    print("\nDue books for today:")
    count = 0
    BorrowDate = datetime.date.today()
    borrowed = ItemBorrowedClass.ItemBorrowed(
        0,"","", 0, BorrowDate, "")
    SelectBorrowerLNameToday = SQLfunctions.SelectBorrowerLNameToday(borrowed)
    SelectBorrowerFNameToday = SQLfunctions.SelectBorrowerFNameToday(borrowed)
    SelectBookIDToday = SQLfunctions.SelectBookIDToday(borrowed)
    SelectBorrowedIDToday = SQLfunctions.SelectBorrowedIDToday(borrowed)
    NewBorrowerLNameToday = [ele[0] for ele in SelectBorrowerLNameToday]
    NewBookIDToday = [ele[0] for ele in SelectBookIDToday]
    NewBorrowedIDToday = [ele[0] for ele in SelectBorrowedIDToday]
    print("Borrowed ID`s of people who are due to hand in books today - ")
    if not NewBorrowedIDToday:
        print("\nThere are no books due today!")
    else:
        for i in NewBorrowedIDToday:
            print(i)
        print("BookID(s) due today")
        for z in NewBookIDToday:
            print(z)
    print("\nBook(s) overdue: ")
    SelectOverDueFName = SQLfunctions.SelectOverDueFName(borrowed)
    SelectOverDueLName = SQLfunctions.SelectOverDueLName(borrowed)
    SelectOverDueID = SQLfunctions.SelectOverDueID(borrowed)
    SelectOverDueBorrowedID = SQLfunctions.SelectOverDueBorrowedID(borrowed)
    NewOverDueBorrowedID = [ele[0] for ele in SelectOverDueBorrowedID]
    NewOverDueID = [ele[0] for ele in SelectOverDueID]
    print("Borrowed ID`s of people who have overdue books - " )
    if not NewOverDueBorrowedID:
        print("\nThere are no books overdue!")
    else:
        for k in NewOverDueBorrowedID:
            print(k)
        print("Book ID`s that are overdue - ")
        for s in NewOverDueID:
            print(s)
    LibMenu()


def Issue():
    book = BookClass.Book(0, "", "", "",
                    "", False, False, False)
    DamagedBookSearch = SQLfunctions.DamagedBookSearch(book)
    print("\nDamaged books:")
    for i in DamagedBookSearch:
        print(list(i)[0])
    print("\nLost books:")
    LostBookSearch = SQLfunctions.LostBookSearch(book)
    for k in LostBookSearch:
        print(list(k)[0])
    print("\nBinned books:")
    BinnedBookSearch = SQLfunctions.BinnedBookSearch(book)
    for q in BinnedBookSearch:
        print(list(q)[0])
    try:    
        addisuue = int(input(
            "Do you wish to add a damaged / lost / binned book (1 for yes and 2 for no): "))
    except ValueError:
        raise ValueError(LibMenu())
    if addisuue == 1:
        try:
            bookid = int(input("Enter the ID of the book you want to input: "))
        except ValueError:
            raise ValueError(LibMenu())
        book = BookClass.Book(bookid, "", "", "",
                "", False, False, False)
        SelectAllIDs = SQLfunctions.SelectAllIDs(book)
        newAllIDs = [ele[0] for ele in SelectAllIDs]
        if bookid not in newAllIDs:
            print("\nBook ID not found!")
            LibMenu()
        else:
            try:
                bld = int(input(
                    "Type 1 to enter damaged book, 2 for lost book and 3 for binned book and 4 to exit to menu: "))
            except ValueError:
                raise ValueError(LibMenu())
            SelectDamagedCheck = SQLfunctions.SelectDamagedCheck(book)
            SelectLostCheck = SQLfunctions.SelectLostCheck(book)
            SelectBinnedCheck = SQLfunctions.SelectBinnedCheck(book)
            if bld == 1:
                if SelectDamagedCheck[0] == True:
                    print("\nBook has already been updated")
                    LibMenu()
                else:
                    AddDamagedBook = SQLfunctions.AddDamagedBook(book)
                    print("\n Book is now damaged on the system")
                    LibMenu()
            elif bld == 2:
                if SelectLostCheck[0] == False:
                    AddLostBook = SQLfunctions.AddLostBook(book)
                    print("\n Book is now set to lost on the system")
                    LibMenu()
                else:
                    print("\nBook has already been updated")
                    LibMenu()
            elif bld == 3:
                if SelectBinnedCheck[0] == False:
                    AddBinnedBook = SQLfunctions.AddBinnedBook(book)
                    print("\n Book is now set to Binned on the system")
                    LibMenu()
                else:
                    print("\nBook has already been updated")
                    LibMenu()
            elif bld == 4:
                print("\nexit to menu")
                LibMenu()
            else:
                print("\nNot in range")
                LibMenu()
    else:
        LibMenu()
# LibMenu()


LibMenu()


# DueBook()


# AddTeacher()
# AddStudent()
"""         
def bookList():
    with sqlite3.connect(DATABASE_NAME) as db:
        cursor = db.cursor()
        cursor.execute("select BookName from Book")
        bn = cursor.fetchall()
        return bn
    if __name__ == "__main__":
        bn = bookList()
        list(bn)
        print(bn)
"""
