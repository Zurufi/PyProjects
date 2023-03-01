#Name: Ali Alzurufi
#Description: Create an ATM using classes
#Date: 12/6/22

class BankAccount:
    #Create the constructor
    def __init__(self):
        self.__balance = 1000
        self.__transCount = 0
    
    #Create the method for deposit
    def deposit(self, amount):
        self.__balance += amount
        self.__transCount += 1

    
    #create the method for withdrawal
    def withdrawal(self, amount):
        if amount % 10 != 0:
            print("Error: Withdrawal amount must be in denominations of $10")
        
        elif self.__balance < amount:
            print("Insufficient funds")

        elif self.__balance >= amount:
            self.__balance -= amount
            self.__transCount += 1

    #create the method for getting the new balance
    def getBalance(self):
        self.__transCount += 1
        return self.__balance


    #create the method for getting the number of transactions
    def numofTrans(self):
        return self.__transCount


#create the menu for ATM choices
def Menu():
    
    print("1. Balance Inquiry")
    print("2. Make a Deposit")
    print("3. Make a Withdrawal")
    print("4. Display Number of Transactions")
    print("5. Exit")
    print()

  


#Main function 
def Main():    
   
    while True:

        Menu()
        checkings = BankAccount()

        #user Input
        userInput = int(input("choice: "))

        #Check for valid user entry
        if(userInput > 5 or userInput <= 0):
            print("Error! Inavlid choice. please try again")
            continue

        #Balance Inquiry
        if(userInput == 1):
            print("Account Balance: $", format(checkings.getBalance(), ',.2f'))

        #Deposit
        elif(userInput == 2): 
            depAmount = float(input("How much funds would you like to deposit? "))
            checkings.deposit(depAmount)
            print("Your overall balance is: $",format(checkings.getBalance(), ',.2f'))


        #Withdrawal
        elif(userInput == 3):
            withdrawlAmount = float(input("How much funds woulds you like to withdrawl? "))
            checkings.withdrawal(withdrawlAmount)

            print("Your overall balance is: $",format(checkings.getBalance(), ',.2f'))


        #Number of Transactions
        elif(userInput == 4):
            print("Total number of transactions: ", checkings.numofTrans())

        # Get user input to see if they would like to make another transaction
        userInput2 = input("Would you like to make another transaction? (Enter Y/N): ")

        if(userInput2 == 'Y' or userInput2 == 'y'):
            continue



        elif(userInput2 == 'N' or userInput2 == 'n'):
            print("Thank you for using this ATM")
            exit(0)


        #exit if user inputs 5
        if(userInput == 5):
            print("Thank you for using this ATM")
            exit(0)


#Call main fucntion
Main()
