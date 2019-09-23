def menu():
    """displays options to select from"""
    print("Please select an option:")
    print("1. Display movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Exit")

def getOption():
    menu()
    choice = int(input("Enter option: "))
    while choice < 1 or choice > 4:
        menu()
        choice = int(input("Enter option: "))

def runProgram():
    getOption()



runProgram()
