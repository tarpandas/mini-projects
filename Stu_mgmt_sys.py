import os

print("""

-------------------------------------------------------------------------
|===____=========================================================____===|
|==|    |=======================================================|    |==|
|--|icon|---------------Student Management System---------------|icon|--|
|==|____|=======================================================|____|==|
|=======================================================================|
-------------------------------------------------------------------------
""")

global listStd      #Making a global list
listStd=["Tarpan Das","Sumit Gupta","Tanmoy Nath","Sumit Bera", "Vishal Kashyap"]    #List of Students

def manageStudent():    #Functions of the student Management Sysytem
    global bye
    bye="\n\n-------------------------------TarpanFR Inc.-------------------------------"
#Printing Interface
    print("""
---------------------------------------------------------------------
Enter 1: To view Student's List
Enter 2: To Add New Student
Enter 3: To Search Student
Enter 4: To Remove Student
        """)
    try:
        userInput=  int(input("Please select any option above: "))      #Using Exceptions For Validation
    except: ValueError:   exit("\nHy! That's not a number")   #Error message
    else:
        print("\n")
        
#Checking using 0ption
    if(userInput == 1):     #This option will print list of students
        print("List Students\n")
        for students in listStd:
            print("=> {}".format(students))

    elif(userInput ==2):    #This option will add new students in then list
        newStd=input("Enter the Student: ")
        if(newStd in listStd):  #This condition checks whether the new studentis in the list or not
            print("\n This Student {} is already in the database".format(newStd))
        else:
            listStd.append(newStd)
            print("\n=>New Student {} is succesfully added.".format(newStd))
            for students in listStd:
                print("=> {}".format(students))
                    
    elif(userInput ==3):    #This option will search student from the list
        srcStd=input("Enter the student name to search: ")
        if(srcStd in listStd):      #This condition searches the student
            print("\nRecord funt of the student {}".format(srcStd))
        else:
            print("\nNo record found of the student {}".format(srcStd))     #Error Message

    elif(userInput ==4):
        rmStd=input("Enter the name of the Student to be removed: ")
        if(rmStd in listStd):
            listStd.remove(rmStd)
            print("The student {} Successfully removed".format(rmStd))
        else:
            print("No student found t=of the name to be removed: ")
            for students in listStd:
                print("=> {}".format(students))

    elif(userInput <1 or userInput >4): #Validating User option
        print("Please Enter valid option")

manageStudent()

def runAgain():     #Making Runable Program
    runAgn = input("\n Want to run again Y/N: ")
    if(runAgn.lower() == 'y'):
        manageStudent()
        runAgain()
    else:
        print(bye)
        quit()

runAgain()
