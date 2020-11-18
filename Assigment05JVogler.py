# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JVOGLER, NOV 15 2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
import os.path

# adjust filepath here
file_path = 'C:\\Users\\VoglerJ\\Documents\\U WASHINGTON PYTHON\\_PythonClass\\Assignment05'
# adjust .txt filename
name_of_file = "ToDoList.txt"
completeName = os.path.join(file_path, name_of_file)

# Process the data
objFile = open(completeName, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"To-Do": lstRow[0], "Priority": lstRow[1].strip()}
    print(dicRow)
    print(dicRow["To-Do"] + '|' + dicRow["Priority"])
    lstTable.append(dicRow)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("To-Do|Priority\n")
        for row in lstTable:
            print(row["To-Do"] ,'|' , row["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        print("What do you need To Do and what is the Priority?")
        name = str(input("To-Do: "))
        value = str(input("Priority: "))
        lstTable.append({"To-Do": name, "Priority": value})
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        print("What To-Do item do you want to remove?")
        removeToDo = str(input("To-Do: "))
        for row in lstTable:
            if row["To-Do"].lower() == removeToDo.lower():
                lstTable.remove(row)
                print("To-Do Removed")
                print(lstTable)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open(completeName, "w")
        for row in lstTable:
            objFile.write(row.get("To-Do")+","+row.get("Priority")+"\n")
        objFile.close()
        print("Data saved")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program

