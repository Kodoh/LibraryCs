import sys
sys.path.append(sys.path[0] + "/Actions")
sys.path.append(sys.path[0] + "/Actions/classes")
import classes.LibStaffClass as LibStaffClass
import SQLfunctions
DATABASE_NAME = "library.db"


def usernameFun():
        usname = input("Please enter Username: ")
        LibS = LibStaffClass.LibStaff(uid,"","","","")
        SelectUsername = SQLfunctions.SelectUsername(LibS)
        if SelectUsername == usname:
            passwordFun()
        else:
            print("Invalid username!")


def passwordFun():
    password = input("Please enter Password: ")
    LibS = LibStaffClass.LibStaff(uid,"","","","")
    SelectPassword = SQLfunctions.SelectPassword(LibS)
    if SelectPassword == password:
        import menu
        menu.LibMenu()
    else:
        print("Invalid password!")

def error():
    sys.exit()

try:
    uid = int(input("Please enter ID: "))
except ValueError:
    raise ValueError(error())
if uid <= 5 and uid >= 1:
    usernameFun()
else:
    print("Invalid ID!")
