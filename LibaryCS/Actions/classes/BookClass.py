class Book:
    __ID = 0
    __ISBN = ""
    __Name = ""
    __IsTaken = False
    __Author = ""
    __IsBinned = False
    __IsLost = False
    __IsDamaged = False

    def __init__(self, BookID=0, ISBN="", Book_Name="", Author="", Book_Taken=False, IsBinned=False,IsLost=False,IsDamaged=False):
        self.__ID = BookID
        self.__ISBN = ISBN
        self.__Name = Book_Name
        self.__IsTaken = Book_Taken
        self.__Author = Author
        self.__IsBinned = IsBinned
        self.__IsLost = IsLost
        self.__IsDamaged = IsDamaged
    def getID(self):
        return self.__ID
    def setISBN(self,ISBN):
        self.__ISBN = ISBN
    def getISBN(self):
        return self.__ISBN
    def setTitle(self,Book_Name):
        self.__Name = BookName
    def getTitle(self):
        return self.__Name
    def setIsTaken(self,IsTaken):
        self.__IsTaken = Book_Taken
    def getIsTaken(self):
        return self.__IsTaken
    def getAuthor(self):
        return self.__Author
    def setAuthor(self,Author):
        self.__Author = Author
    def setIsBinned(self,IsBinned):
        self.__IsBinned = IsBinned
    def getIsBinned(self):
        return self.__IsBinned
    def setIsLost(self,IsLost):
        self.__IsLost = self.IsLost
    def getIsLost(self):
        return self.__IsLost
    def setDamaged(self,IsDamaged):
        self.__IsDamaged = IsDamaged
    def getIsDamaged(self):
        return self.__IsDamaged