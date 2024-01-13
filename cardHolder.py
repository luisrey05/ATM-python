class cardHolder():
    def __init__(self, cardNum, pin, firstname, lastname, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def get_cardNum(self):
        return self.cardNum
    def get_pin(self):
        return self.pin

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_balance(self):
        return self.balance

    def set_cardNum(self, num):
        self.cardNum = num

    def set_pin(self, pin):
        self.pin = pin

    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_balance(self, balance):
        self.balance = balance

    def print_out(self):
        print("Card #: ", self.cardNum)
        print("Pin : ", self.pin)
        print("First Name : ", self.firstname)
        print("Last Name : ", self.lastname)
        print("Balance : ", self.balance)
