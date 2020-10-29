import datetime
class ItemBorrowed:
    __BorrowedID = 0
    __BorrowedFName = ""
    __BorrowedLName = ""
    __BookID = 0
    __BorrowDate = ""                  
    __DueDate = ""
    def __init__(self, BorrowedID, BorrowedFName, BorrowedLName, BookID, BorrowDate, DueDate):
        self.__BorrowedID = BorrowedID 
        self.__BorrowedFName = BorrowedFName
        self.__BorrowedLName = BorrowedLName 
        self.__BookID = BookID
        self.__BorrowDate = BorrowDate 
        self.__DueDate = DueDate 
    def getBorrowedID(self):
        return self.__BorrowedID 
    def setBorrowedFName(self,BorrowedFName):
        __BorrowedFName = BorrowedFName
    def getBorrowedFName(self):
        return self.__BorrowedFName
    def setBorrowedLName(self,BorrowedLName):
        __BorrowedLName = BorrowedLName
    def getBorrowedLName(self):
        return self.__BorrowedLName
    def setBookID(self,BookID):
        __BookID = BookID
    def getBookID(self):
        return self.__BookID
    def getBorrowedDate(self):
        return self.__BorrowDate
    def setBorrowedDate(self,BorrowDate):
        __BorrowDate = datetime.date.today()
    def getDueDate(self):
        return self.__DueDate
    def setDueDate(self,DueDate):
        __DueDate = DueDate