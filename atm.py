class Atm:
    def _init_(self,cardnumber,pin, phonenumber, name, balance):
        self.name = name
        self.phonenumber = phonenumber
        sef.cardnumber = cardnumber
        self.pin = pin
        self.balance = balance
    def printdetails(self, name, phonenumber, cardnumber, pin)
        print(name,phonenumber,cardnumber,pin)
    def check_balance(self, balance)
        print("Your balance is",balance)
    def withdrawal(self,balance)
        wd = int(input("How much do you want to withdraw"))
        balance = balance - wd
     def deposit(self,balance)
        d = int(input("How much do you want to deposit"))
        balance = balance + d   
    
name1 = input("Please enter your name: ")
pn = int(input("Please enter your phonenumber: "))
cn = int(input("Please enter your cardnumber: ")
pin1 = int(input("Please enter your pin: "))
b = int(input("Please enter your balance: "))

user = Atm(name1, pn, cn, pin1)

         
