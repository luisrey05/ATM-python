import os
from datetime import datetime
from cardHolder import cardHolder
import atm

def main():

    # Creating directory and current date and time variables
    currentDirectory = os.getcwd()
    userName = os.getlogin()
    now = datetime.now()
    date = now.strftime("%B %d, %Y @ %I:%M:%S")

    # Displaying current directory, date and time
    print(currentDirectory)
    print(f'Programmer: {userName}')
    print(f'Capstone project {date}\n')


    current_user = cardHolder("","","","","")

    list_of_cardHolder = []
    list_of_cardHolder.append(cardHolder("123456789",1234, "John", "Griffith",0))
    list_of_cardHolder.append(cardHolder("987654321", 4321, "Luis", "Villalba", 10.10))
    list_of_cardHolder.append(cardHolder("543216789", 1324, "Maria", "Guadalupe", 200.30))
    list_of_cardHolder.append(cardHolder("987612345", 1245, "Jose", "Garcia", 500.50))
    list_of_cardHolder.append(cardHolder("132465798", 6996, "Carlos", "Aguilar", .50))

    print("Welcome to Chase ATM.")
    debitCardNum = ""
    while True:
        try:

            debitCardNum = input("Please insert your debit card: ")
            debitMatch = [holder for holder in list_of_cardHolder if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again.")
        except:
            print("Card number not recognized. Please try again.")



    while True:
        try:
            userPin = int(input("Please enter your pin: ").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again")
        except:
            print('Invalid PIN. Please try again.')

    print("Welcome ", current_user.get_firstname(),' :)\n')
    option = 0

    while True:
        atm.print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")


        if(option ==1):
            atm.deposit(current_user)
        elif(option == 2):
            atm.withdraw(current_user)
        elif(option == 3):
            atm.check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0

    print("Thank you have a nice day.")

if __name__ == '__main__':
    main()