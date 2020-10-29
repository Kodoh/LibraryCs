class Borrower:
    __BorrowerID = 0
    __FirstName = ""
    __Surname = ""
    __Address = ""
    __StaffYN = False
    def __init__(self, BorrowerID, FirstName, Surname, Address, StaffYN=False):
        self.__BorrowerID = BorrowerID
        self.__FirstName = FirstName
        self.__Surname = Surname 
        self.__Address = Address
        self.__StaffYN = StaffYN 
    def getBorrowerID(self):
        return self.__BorrowerID
    def setFirstName(self,FirstName):
        __FirstName = FirstName
    def getFirstName(self):
        return self.__FirstName
    def setSurname(self,Surname):
        __Surname = Surname
    def getSurname(self):
        return self.__Surname
    def setAddress(self,Address):
        __Address = Address
    def getAddress(self):
        return self.__Address
    def setStaffYN(self,StaffYN):
        __StaffYN = StaffYN
    def getStaffYN(self):
        return self.__StaffYN    