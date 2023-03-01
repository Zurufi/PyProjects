#Ali Alzurufi

#This program will be an airline seat selection program


#Create list
Seats = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']

fcFull = " "
eFull = " "

#Function for first class seats
def firstClass(userChoice):

    #Get user input for seat selection
    firstC = int(input("Please select your seat number (1 - 5): "))

    #Check if seat is taken or not
    while(Seats[firstC-1] == 'X'):
        print("This seat is not available. Please select another seat")
        firstC = int(input("Please select your seat number (1 - 5): "))

    Seats[firstC - 1] = 'X'

    #Check if seat is in first class or not
    while(firstC > 5):
        print("This is not in the First Class section.")
        firstC = int(input("Please select your seat number (1 - 5): "))

    print()
    print()
    menu()
   


#Function for Economy class
def Economy(userChoice):

    #Get user input for seat selection
    economy = int(input("Please select your seat number (6 - 10): "))

    #Check if seat is taken or not
    while(Seats[economy-1] == 'X'):
        print("This seat is not available. Please select another seat")
        economy = int(input("Please select your seat number (6 - 10): "))

    Seats[economy-1] = 'X'

    #Check if seat is in economy class
    while(economy < 6):
        print("This is not in the Economy section.")
        economy = int(input("Please select your seat number (6 - 10): "))
    

    print()
    print()
    menu()


#Function for the menu
def menu():
 

    #Display menu options and seating charts
    print("1. First class"        "(Rows: 1 to 5)")

    #Check if section is full
    if 'A' not in Seats[:5]:
        print("Full")
        print()
    
    print("2. Economy"            "(Rows: 6 to 10)")

    #Check if section is full
    if 'A' not in Seats[5:]:
        print("Full")
        print()
        
    print("3. Exit")

    print()
    print("Seating Chart: ", Seats)
    print()

    #Get user input for which option they would like (ex: 1, 2, or 3)
    userChoice = int(input("Enter a choice: "))

    print()
    
    #Call functions based on user input or quit program
    if(userChoice == 1):
        firstClass(userChoice)
    elif(userChoice == 2):
        Economy(userChoice)
    elif(userChoice == 3):
        print("Thanks for using this airline, goodbye!")
        exit()

       



#Display menu for first time
menu()
    
