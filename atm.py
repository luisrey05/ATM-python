from cardHolder import cardHolder

def print_menu():
    print("Please choose from one of the following options...")
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Show Balance')
    print('4. Exit')


def deposit(cardHolder):
    try:
        deposit = float(input("\nHow much $$ would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print(f"Thank you for your $$. Your new balance is: ${(cardHolder.get_balance()):.2f}")
    except:
        print("Invalid input")


def withdraw(cardHolder):
    try:
        withdraw = float(input("\nHow much $$ would you like to withdraw: "))
        if cardHolder.get_balance() < withdraw:
            print("Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go! Thank you :)")
    except:
        print("Invalid input")


def check_balance(cardHolder):
    print(f"\nYour current balance is: ${cardHolder.get_balance():.2f}")



