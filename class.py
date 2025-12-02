class BankAccount:
    def __init__(self, Account_number, balance, owners_name, date_opened):
        self.account_number = Account_number
        self.balance = 0git
        self.owners_name = owners_name
        self.date_opened = date_opened
        print("Welcome")
    def deposit(self, amount):
        amount = float(input("Enter the Amount you want to deposit: "))
        if amount < 0:
            print("you can't deposit a negative amount")
        else:
            self.balance += amount
        print(f"You have deposited Ksh. {amount}")
        
    def withdraw(self, amount):
        amount = float(input("Enter the Amount you want to withdraw: "))
        if self.balance < amount:
            print("insufficient funds")
        else:
            self.balance -= amount
            print(f"You have withdrawn Kshs. {amount}")
                      
    def display_info(self):
          print(f"Your Available Balance is Kshs. {self.balance}")
                    
                    
                      
        
            