class LibStaff:
    __LibID = 0
    __Name_First = ""
    __Name_Last = ""
    __Username = ""
    __Password = ""
    def __init__(self, LibID, Name_First, Name_Last, Username, Password):
        self.__LibID = LibID
        self.__Name_First = Name_First
        self.__Name_Last = Name_Last 
        self.__Username = Username 
        self.__Password = Password 
    def getLibID(self):
        return self.__LibID
    def setFirstName(self,Name_First):
        self.__Name_First = Name_First
    def getFirstName(self):
        return self.__Name_First 
    def setLastName(Name_Last):
        self.__Name_Last = Name_Last
    def getLastName(self):
        return self.__Name_Last
    def setUsername(self,Username):
        self.__Username = Username
    def getUsername(self):
        return self.__Username
    def setPassword(self,Password):
        self.__Password = Password
    def getPassword(self):
        return self.__Password